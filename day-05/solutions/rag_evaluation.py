"""Day 05 Reference Solution: Automated RAG Benchmark & Evaluation Engine."""

import sys
import os
import json
import logging
from typing import List, Dict, Any

# Link to shared libraries and Day 04 RAG pipeline
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
# Import Day 04 pipeline dynamically
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "day-04", "solutions")))
from rag_pipeline import InsuranceRAGPipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Ground-truth evaluation benchmark
EVALUATION_BENCHMARK = [
    {
        "question": "What is the deductible for collision claims and the vanishing deductible rule?",
        "expected_doc_id": "KB-101",
        "description": "Auto insurance policy terms"
    },
    {
        "question": "Is water damage from repeated pipe leaks covered under home insurance?",
        "expected_doc_id": "KB-102",
        "description": "Homeowners water damage exclusion"
    },
    {
        "question": "What are the rules and timeframe for commercial business interruption compensation?",
        "expected_doc_id": "KB-103",
        "description": "Commercial business interruption policy"
    },
    {
        "question": "What is the maximum medical evacuation coverage on travel guard policies?",
        "expected_doc_id": "KB-104",
        "description": "Travel insurance medical limit"
    },
    {
        "question": "Within how many hours must a cyber liability breach be reported?",
        "expected_doc_id": "KB-105",
        "description": "Cyber defense reporting mandate"
    }
]


def evaluate_rag_pipeline(pipeline: InsuranceRAGPipeline, benchmark: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Runs automated retrieval and generation evaluation."""
    total = len(benchmark)
    hits_at_1 = 0
    hits_at_2 = 0
    reciprocal_ranks = []
    evaluation_records = []

    print("\n" + "=" * 75)
    print("EXECUTING AUTOMATED RAG EVALUATION BENCHMARK")
    print("=" * 75)

    for idx, item in enumerate(benchmark, start=1):
        q = item["question"]
        expected = item["expected_doc_id"]

        retrieved = pipeline.retrieve(q, top_k=2)
        retrieved_ids = [doc["id"] for doc in retrieved]

        # Calculate rank
        rank = 0
        if expected in retrieved_ids:
            rank = retrieved_ids.index(expected) + 1

        is_hit_1 = rank == 1
        is_hit_2 = rank > 0 and rank <= 2

        if is_hit_1:
            hits_at_1 += 1
        if is_hit_2:
            hits_at_2 += 1

        reciprocal_rank = 1.0 / rank if rank > 0 else 0.0
        reciprocal_ranks.append(reciprocal_rank)

        answer = pipeline.answer_question(q)
        # Check source grounding presence
        has_citation = f"[{expected}]" in answer or expected in answer

        record = {
            "test_id": idx,
            "question": q,
            "expected_id": expected,
            "retrieved_ids": retrieved_ids,
            "rank": rank,
            "reciprocal_rank": reciprocal_rank,
            "grounded_citation_present": has_citation,
            "status": "PASS" if is_hit_2 else "FAIL"
        }
        evaluation_records.append(record)

        print(f"\n[Test #{idx}] {item['description']}")
        print(f"  Question: '{q[:60]}...'")
        print(f"  Expected: {expected} | Retrieved: {retrieved_ids} | Rank: {rank} -> {record['status']}")

    hit_rate_at_1 = round(hits_at_1 / total, 4)
    hit_rate_at_2 = round(hits_at_2 / total, 4)
    mrr = round(sum(reciprocal_ranks) / total, 4)

    summary = {
        "total_test_cases": total,
        "hits_at_1": hits_at_1,
        "hit_rate_at_1": hit_rate_at_1,
        "hits_at_2": hits_at_2,
        "hit_rate_at_2": hit_rate_at_2,
        "mean_reciprocal_rank_mrr": mrr,
        "benchmark_records": evaluation_records
    }
    return summary


def main():
    pipeline = InsuranceRAGPipeline()
    report = evaluate_rag_pipeline(pipeline, EVALUATION_BENCHMARK)

    print("\n" + "=" * 75)
    print("RAG RETRIEVAL & GROUNDING EVALUATION SCORECARD")
    print("=" * 75)
    print(f"Total Test Cases Evaluated : {report['total_test_cases']}")
    print(f"Hit Rate @ 1 (Top Pick)    : {report['hit_rate_at_1'] * 100:.1f}%")
    print(f"Hit Rate @ 2 (Top 2 Recall): {report['hit_rate_at_2'] * 100:.1f}%")
    print(f"Mean Reciprocal Rank (MRR) : {report['mean_reciprocal_rank_mrr']}")
    print("=" * 75)


if __name__ == "__main__":
    main()
