import ollama


def generate_answer(query, context):

    prompt = f"""
    Answer using ONLY context.

    Context:
    {context}

    Question:
    {query}
    """

    response = ollama.chat(

        model="llama3",

        messages=[{
            "role": "user",
            "content": prompt
        }],

        options={          # ⭐ generation settings go here
            "temperature": 0
        }

    )

    return response["message"]["content"]
