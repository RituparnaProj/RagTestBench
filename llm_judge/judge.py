import ollama
import json

def llm_judge(question, expected, actual):

    prompt = f"""
Score answer correctness.

Return JSON only.

Question:
{question}

Expected:
{expected}

Actual:
{actual}

Return:
{{"score":0-1}}
"""

    res = ollama.chat(
        model="llama3",
        messages=[{
            "role": "user",
            "content": prompt
        }],
        options={"temperature": 0}
    )

    text = res["message"]["content"]

    try:
        parsed = json.loads(text)
        return float(parsed["score"])
    except:
        return 0.0
