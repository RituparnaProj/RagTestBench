from ContextFramework.validator.similarity_validator import validate_similarity
from ContextFramework.llm_judge.judge import llm_judge

def ragas_score(question, expected, actual):

    # 1. Semantic similarity
    similarity_score = validate_similarity(
        expected,
        actual
    )

    # 2. LLM Judge score
    judge_score = llm_judge(
        question,
        expected,
        actual
    )

    # 3. Weighted final score
    final_score = (
        0.6 * similarity_score +
        0.4 * judge_score
    )

    return {
        "similarity_score": round(similarity_score, 3),
        "judge_score": round(judge_score, 3),
        "final_score": round(final_score, 3)
    }
