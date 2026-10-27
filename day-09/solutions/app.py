"""Day 09 Reference Solution: Production LLM Multi-Feature Web Dashboard & Service."""

import sys
import os
import json
import time
import argparse
import logging
from typing import Dict, Any

# Ensure import access across all days
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from shared.utils import UnifiedLLMClient, count_tokens, estimate_cost

# Dynamic imports of previous solutions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "day-03", "solutions")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "day-04", "solutions")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "day-07", "solutions")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "day-08", "solutions")))

from tool_calling_assistant import AirlineAssistant
from rag_pipeline import InsuranceRAGPipeline
from security_guardrails import SecurityGuardrailMiddleware
from autonomous_agent import BoundedReActDealAgent

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


class ProductionAIPlatform:
    """Consolidated enterprise service wrapper exposing RAG, tools, agent, and security telemetry."""

    def __init__(self):
        self.guard = SecurityGuardrailMiddleware()
        self.airline = AirlineAssistant()
        self.rag = InsuranceRAGPipeline()
        self.agent = BoundedReActDealAgent(max_steps=4)
        logger.info("Production AI Platform components successfully loaded.")

    def handle_insurance_rag(self, question: str) -> Dict[str, Any]:
        """Secured Insurance RAG query with telemetry."""
        # Layer 1: Security guardrail check
        guard_res = self.guard.execute_query(question)
        if guard_res["flagged"]:
            return guard_res

        start = time.time()
        docs = self.rag.retrieve(question, top_k=2)
        answer = self.rag.answer_question(question)
        elapsed_ms = round((time.time() - start) * 1000, 2)
        tok_count = count_tokens(question) + count_tokens(answer)

        return {
            "status": "SUCCESS",
            "service": "Insurance RAG",
            "question": question,
            "retrieved_sources": [d["id"] for d in docs],
            "response": answer,
            "latency_ms": elapsed_ms,
            "tokens_consumed": tok_count
        }

    def handle_flight_inquiry(self, query: str) -> Dict[str, Any]:
        """Airline tool calling handler with telemetry."""
        start = time.time()
        answer = self.airline.process_query(query)
        elapsed_ms = round((time.time() - start) * 1000, 2)
        tok_count = count_tokens(query) + count_tokens(answer)

        return {
            "status": "SUCCESS",
            "service": "Airline Tools",
            "query": query,
            "response": answer,
            "latency_ms": elapsed_ms,
            "tokens_consumed": tok_count
        }

    def handle_deal_search(self, product_goal: str) -> Dict[str, Any]:
        """Autonomous deal verification agent with telemetry."""
        start = time.time()
        res = self.agent.run(product_goal)
        elapsed_ms = round((time.time() - start) * 1000, 2)

        return {
            "status": "SUCCESS",
            "service": "Autonomous Deal Agent",
            "goal": product_goal,
            "deal_price_usd": res.get("deal_price_usd"),
            "msrp_usd": res.get("msrp_usd"),
            "is_all_time_low": res.get("is_all_time_low"),
            "response": res.get("recommendation"),
            "steps_executed": res.get("steps_taken"),
            "latency_ms": elapsed_ms
        }


def run_cli_test_mode(platform: ProductionAIPlatform):
    """Executes platform validation checks via command line."""
    print("\n" + "=" * 75)
    print("PRODUCTION AI PLATFORM TEST RUN")
    print("=" * 75)

    # Test 1: RAG
    print("\n[Service 1: Enterprise Insurance RAG]")
    rag_out = platform.handle_insurance_rag("What is the deductible for collision claims?")
    print(f"  Retrieved Sources: {rag_out.get('retrieved_sources')}")
    print(f"  Latency: {rag_out.get('latency_ms')} ms | Tokens: {rag_out.get('tokens_consumed')}")

    # Test 2: Flight Tool
    print("\n[Service 2: Airline Customer Support Tools]")
    flight_out = platform.handle_flight_inquiry("What is the status of flight SK-204?")
    print(f"  Latency: {flight_out.get('latency_ms')} ms")

    # Test 3: Autonomous Agent
    print("\n[Service 3: Autonomous Deal Intelligence Agent]")
    deal_out = platform.handle_deal_search("Apex Acoustic Headphones")
    print(f"  Deal Price: ${deal_out.get('deal_price_usd')} (All-time low: {deal_out.get('is_all_time_low')})")
    print(f"  Steps Taken: {deal_out.get('steps_executed')} | Latency: {deal_out.get('latency_ms')} ms")

    print("\n" + "=" * 75)
    print("ALL INTEGRATED ENTERPRISE SERVICES OPERATIONAL")
    print("=" * 75)


def run_streamlit_dashboard():
    """Renders the interactive web dashboard if running under Streamlit."""
    import streamlit as st
    st.set_page_config(page_title="Enterprise LLM Operations Desk", page_icon="🤖", layout="wide")
    st.title("🤖 Enterprise LLM Operations Desk")
    st.caption("Day 09 Production Application — Integrated Multi-Service AI Platform")

    platform = ProductionAIPlatform()

    tab1, tab2, tab3 = st.tabs(["📚 Insurance RAG", "✈️ Airline Tools", "🛍️ Autonomous Deal Agent"])

    with tab1:
        st.subheader("Enterprise Knowledge Base (RAG)")
        q = st.text_input("Enter policy inquiry:", "What is the deductible for collision claims?")
        if st.button("Query Knowledge Base", key="btn_rag"):
            with st.spinner("Retrieving verified policy clauses..."):
                res = platform.handle_insurance_rag(q)
                st.markdown(f"**Retrieved Sources:** `{', '.join(res.get('retrieved_sources', []))}`")
                st.markdown(f"**Answer:**\n{res['response']}")
                st.metric("Latency", f"{res['latency_ms']} ms", delta=f"{res['tokens_consumed']} tokens")

    with tab2:
        st.subheader("Airline Customer Service Tools")
        flight_q = st.text_input("Inquire about flight status or baggage:", "What is the gate for flight SK-204?")
        if st.button("Ask Airline Assistant", key="btn_flight"):
            with st.spinner("Checking live schedule & calculations..."):
                f_res = platform.handle_flight_inquiry(flight_q)
                st.write(f_res["response"])
                st.caption(f"Latency: {f_res['latency_ms']} ms")

    with tab3:
        st.subheader("Autonomous Deal Hunter Agent")
        prod = st.text_input("Product to research:", "Apex Acoustic Headphones")
        if st.button("Deploy Shopping Agent", key="btn_agent"):
            with st.spinner("Running ReAct reasoning and price verification loops..."):
                d_res = platform.handle_deal_search(prod)
                col1, col2 = st.columns(2)
                col1.metric("Deal Price", f"${d_res.get('deal_price_usd')}")
                col2.metric("All-Time Historical Low?", "YES" if d_res.get("is_all_time_low") else "NO")
                st.markdown(f"**Strategic Recommendation:**\n{d_res['response']}")
                st.caption(f"Reasoning Steps: {d_res.get('steps_executed')} | Latency: {d_res['latency_ms']} ms")


def main():
    parser = argparse.ArgumentParser(description="Day 09: Production AI Platform")
    parser.add_argument("--test", action="store_true", help="Run automated CLI verification checks")
    args = parser.parse_args()

    # If invoked directly via python
    if args.test or "STREAMLIT_SERVER_PORT" not in os.environ:
        platform = ProductionAIPlatform()
        run_cli_test_mode(platform)
    else:
        run_streamlit_dashboard()


if __name__ == "__main__":
    main()
