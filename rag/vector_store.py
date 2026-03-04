from langchain_community.vectorstores import FAISS
from rag.embedder import get_embeddings


def create_vectorstore(docs):

    embeddings = get_embeddings()

    vectorstore = FAISS.from_texts(
        docs,
        embedding=embeddings
    )

    return vectorstore
