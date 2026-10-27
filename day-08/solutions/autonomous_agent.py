"""Day 08 Reference Solution: Bounded Autonomous ReAct Deal Agent."""

import sys
import os
import json
import logging
from typing import Dict, Any, List

# Link to shared libraries
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from shared.utils import UnifiedLLMClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Simulated eCommerce catalog & historical records
CATALOG_DB = {
    "PRD-101": {
        "title": "UltraClean Robot Vacuum X5",
        "msrp_usd": 499.99,
        "current_deal_usd": 349.99,
        "historical_low_usd": 329.00,
        "competitor_price_usd": 369.00,
        "in_stock": True
    },
    "PRD-102": {
        "title": "Apex Acoustic Noise-Cancelling Headphones",
        "msrp_usd": 249.99,
        "current_deal_usd": 169.15,
        "historical_low_usd": 179.99,  # All-time low!
        "competitor_price_usd": 219.00,
        "in_stock": True
    }
}


class BoundedReActDealAgent:
    """Autonomous deal verification agent utilizing bounded Thought-Action-Observation loops."""

    def __init__(self, max_steps: int = 4):
        self.max_steps = max_steps
        self.client = UnifiedLLMClient()
        self.scratchpad: List[Dict[str, str]] = []

    # Available Tools
    def search_catalog(self, query: str) -> Dict[str, Any]:
        """Tool 1: Searches the product database."""
        q = query.lower()
        for pid, data in CATALOG_DB.items():
            if q in data["title"].lower() or any(w in data["title"].lower() for w in q.split()):
                return {"found": True, "product_id": pid, "title": data["title"], "deal_price": data["current_deal_usd"], "msrp": data["msrp_usd"]}
        return {"found": False, "error": f"No product matching '{query}' found."}

    def get_price_history(self, product_id: str) -> Dict[str, Any]:
        """Tool 2: Looks up 12-month historical lowest price."""
        if product_id in CATALOG_DB:
            item = CATALOG_DB[product_id]
            return {
                "product_id": product_id,
                "historical_low_usd": item["historical_low_usd"],
                "competitor_price_usd": item["competitor_price_usd"],
                "is_all_time_low": item["current_deal_usd"] <= item["historical_low_usd"]
            }
        return {"error": f"Invalid product ID: {product_id}"}

    def run(self, user_goal: str) -> Dict[str, Any]:
        """Executes bounded autonomous planning and tool dispatch loop."""
        logger.info(f"Initiating autonomous agent loop for goal: '{user_goal}'")
        self.scratchpad = []

        step = 1
        # Step 1: Catalog Search
        thought_1 = f"To evaluate the deal for '{user_goal}', I need to find its current listed price."
        obs_1 = self.search_catalog(user_goal)
        self.scratchpad.append({
            "step": step,
            "thought": thought_1,
            "action": f"search_catalog('{user_goal}')",
            "observation": json.dumps(obs_1)
        })

        if not obs_1.get("found"):
            return {
                "goal": user_goal,
                "steps_taken": step,
                "recommendation": f"Product '{user_goal}' not found in active merchant catalog.",
                "scratchpad": self.scratchpad
            }

        step += 1
        pid = obs_1["product_id"]

        # Step 2: Historical & Competitor Comparison
        thought_2 = f"Product found ({obs_1['title']}). Now I must check historical lowest price and competitor rates."
        obs_2 = self.get_price_history(pid)
        self.scratchpad.append({
            "step": step,
            "thought": thought_2,
            "action": f"get_price_history('{pid}')",
            "observation": json.dumps(obs_2)
        })

        step += 1
        # Step 3: Synthesis & Strategic Recommendation
        thought_3 = "I have sufficient data on current price, historical low, and competitor matching. I can now synthesize the final recommendation."

        synthesis_prompt = (
            f"USER GOAL: {user_goal}\n\n"
            f"AGENT REASONING TRACE:\n{json.dumps(self.scratchpad, indent=2)}\n\n"
            "Produce an expert shopper deal recommendation: state the discount percentage, whether it beats historical low, and whether to BUY NOW or WAIT."
        )

        final_response = self.client.complete(
            prompt=synthesis_prompt,
            system_prompt="You are a smart shopping intelligence agent. Give a concise, decisive recommendation."
        )

        return {
            "goal": user_goal,
            "product": obs_1["title"],
            "steps_taken": step,
            "deal_price_usd": obs_1["deal_price"],
            "msrp_usd": obs_1["msrp"],
            "is_all_time_low": obs_2.get("is_all_time_low", False),
            "recommendation": final_response,
            "scratchpad": self.scratchpad
        }


def main():
    agent = BoundedReActDealAgent(max_steps=4)

    test_goals = [
        "Apex Acoustic Headphones",
        "UltraClean Robot Vacuum"
    ]

    print("\n" + "=" * 75)
    print("BOUNDED AUTONOMOUS REACT DEAL AGENT DEMO")
    print("=" * 75)

    for goal in test_goals:
        print(f"\n>> AGENT OBJECTIVE: Evaluate deal on '{goal}'")
        result = agent.run(goal)
        print(f"   Steps Executed: {result['steps_taken']} (Bounded Ceiling: 4)")
        print(f"   Product Identified: {result.get('product')}")
        print(f"   Deal Price: ${result.get('deal_price_usd')} (MSRP: ${result.get('msrp_usd')})")
        print(f"   All-Time Historical Low: {'YES' if result.get('is_all_time_low') else 'NO'}")
        print("\n   [ReAct Trace Summary]:")
        for s in result["scratchpad"]:
            print(f"     Step {s['step']}: {s['thought']}")
            print(f"       -> Action: {s['action']}")
        print(f"\n   [Final Recommendation]:\n   {result['recommendation']}\n" + "-" * 75)


if __name__ == "__main__":
    main()
