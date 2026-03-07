import json

from rag.rag_pipeline import rag_answer
from ragas_eval.ragas_score import ragas_score
from guardrails.guardrail import apply_guardrails
from utils.logger import get_logger

logger = get_logger()


def run():

    # Load dataset
    with open("dataset/golden_dataset.json", "r") as f:
        test_data = json.load(f)

    results = []

    for test in test_data:

        question = test["question"]
        expected = test["expected_answer"]

        #print("\n==============================")
        #print("Question:", question)

        logger.info("==============================")
        logger.info(f"Question: {question}")

        # Guardrails check
        is_safe, message = apply_guardrails(question)

        if not is_safe:
            print("Blocked by Guardrail:", message)
            continue

        # RAG answer
        actual = rag_answer(question)

        #print("Actual Answer:", actual)
        logger.info(f"Actual Answer: {actual}")

        # RAGAS scoring
        scores = ragas_score(
            question,
            expected,
            actual
        )

        # print("Scores:", scores)
        logger.info(f"Scores: {scores}")

        results.append({
            "question": question,
            "scores": scores
        })

    # print("\n========= FINAL SUMMARY =========")
    logger.info("========= FINAL SUMMARY =========")

    for r in results:
        #print(r)
        logger.info(r)


if __name__ == "__main__":
    run()
