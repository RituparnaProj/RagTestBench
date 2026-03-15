
from rag.vector_store import load_vectorstore
from rag.retriever import get_retriever
from rag.generator import generate_answer



def load_documents():
    """
    In real production, this would load PDFs, DB, etc.
    For now, hardcoded knowledge base.
    """

    docs = [
         "Paris is the capital of France.",
        "William Shakespeare wrote Hamlet.",
        "Python is a programming language."
    ]

    return docs


def rag_answer(question):
    # 1️⃣ Load knowledge base
    docs = load_documents()

    # 2️⃣ Create vector store
    vectorstore = load_vectorstore(docs)

    # 3️⃣ Retrieve relevant docs
    retriever = get_retriever(vectorstore)
    retrieved_docs = retriever.invoke(question)

    # 4️⃣ Build context
    context = "\n".join(doc.page_content for doc in retrieved_docs)

    # 5️⃣ Generate answer
    answer = generate_answer(context, question)

    return answer
    