"""Day 03 Reference Solution: Airline Customer Service Tool Calling Assistant."""

import sys
import os
import json
import re
import logging
from typing import Dict, Any, Optional

# Link to shared libraries
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from shared.utils import UnifiedLLMClient, count_tokens, estimate_cost

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


class AirlineAssistant:
    def __init__(self, data_file: Optional[str] = None):
        if not data_file:
            data_file = os.path.join(os.path.dirname(__file__), "..", "..", "shared", "sample_data", "flight_data.json")
        with open(data_file, "r", encoding="utf-8") as f:
            self.db = json.load(f)
        self.client = UnifiedLLMClient()
        logger.info(f"AirlineAssistant initialized with {len(self.db['flights'])} flights in database.")

    def lookup_flight(self, flight_number: str) -> Dict[str, Any]:
        """Tool 1: Looks up real-time status and gate for a flight."""
        normalized = flight_number.upper().strip().replace(" ", "-")
        for f in self.db["flights"]:
            if f["flight_number"].upper() == normalized or normalized in f["flight_number"].upper():
                return {"found": True, "details": f}
        return {"found": False, "error": f"Flight code '{flight_number}' not found in active schedule."}

    def calculate_baggage_fee(self, bag_count: int, total_weight_kg: float) -> Dict[str, Any]:
        """Tool 2: Computes baggage fees and overweight penalties."""
        if bag_count <= 0:
            return {"total_fee_usd": 0.0, "message": "No checked bags declared."}

        fees = self.db["baggage_fees"]
        first_bag = fees["first_checked_bag_usd"]
        second_bag = fees["second_checked_bag_usd"] if bag_count >= 2 else 0.0
        extra_bags = max(0, bag_count - 2) * 60.0

        # Standard allowance is 23kg per bag
        free_weight_allowance = bag_count * 23.0
        overweight_kg = max(0.0, total_weight_kg - free_weight_allowance)
        overweight_charge = overweight_kg * fees["overweight_fee_per_kg_usd"]
        total = first_bag + second_bag + extra_bags + overweight_charge

        return {
            "bag_count": bag_count,
            "total_weight_kg": total_weight_kg,
            "base_baggage_fee_usd": first_bag + second_bag + extra_bags,
            "overweight_kg": round(overweight_kg, 1),
            "overweight_surcharge_usd": round(overweight_charge, 2),
            "total_fee_usd": round(total, 2)
        }

    def process_query(self, user_query: str) -> str:
        """Determines tool requirement, dispatches execution, and formats response."""
        logger.info(f"Processing query: '{user_query}'")

        # Intent detection: Check for flight query
        flight_match = re.search(r"SK-?\s*(\d{3})", user_query, re.IGNORECASE)
        bag_match = re.search(r"(\d+)\s*(?:bags?|luggage|suitcases?)", user_query, re.IGNORECASE)
        weight_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:kg|kilos|pounds|lbs)", user_query, re.IGNORECASE)

        tool_results = {}
        if flight_match:
            f_code = f"SK-{flight_match.group(1)}"
            tool_results["flight_status"] = self.lookup_flight(f_code)

        if bag_match:
            count = int(bag_match.group(1))
            weight = float(weight_match.group(1)) if weight_match else (count * 20.0)
            tool_results["baggage_calculation"] = self.calculate_baggage_fee(count, weight)

        # Synthesize final response via LLM
        system_prompt = (
            "You are SkyLine Airways' courteous, professional customer support agent. "
            "Use the provided tool calculation results below to directly and warmly answer the customer's question. "
            "Never fabricate gate numbers, schedules, or prices not present in the tool results."
        )

        synthesis_input = (
            f"Customer Question: '{user_query}'\n\n"
            f"Verified Database Tool Results: {json.dumps(tool_results, indent=2)}\n\n"
            "Formulate a clear, direct, and welcoming customer service answer:"
        )

        response = self.client.complete(
            prompt=synthesis_input,
            system_prompt=system_prompt,
            temperature=0.3
        )
        return response


def main():
    assistant = AirlineAssistant()

    test_queries = [
        "Can you tell me the gate and current status for flight SK-204?",
        "I'm travelling with 2 bags that weigh 52 kg in total. How much will I need to pay?",
        "What is the status of flight SK-999?",
    ]

    print("\n" + "=" * 75)
    print("AIRLINE AI CUSTOMER SERVICE ASSISTANT (TOOL CALLING DEMO)")
    print("=" * 75)

    for q in test_queries:
        print(f"\n>> USER: {q}")
        reply = assistant.process_query(q)
        print(f">> ASSISTANT:\n{reply}\n" + "-" * 75)


if __name__ == "__main__":
    main()
