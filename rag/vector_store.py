import os
from langchain_community.vectorstores import FAISS
from rag.embedder import get_embeddings

INDEX_PATH = "faiss_index"


def load_vectorstore(docs):

    embeddings = get_embeddings()

    if os.path.exists(INDEX_PATH):

        print("Loading existing FAISS index...")

        vectorstore = FAISS.load_local(
            INDEX_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    else:

        print("FAISS index not found. Creating new index...")

        vectorstore = FAISS.from_texts(
            docs,
            embedding=embeddings
        )

        vectorstore.save_local(INDEX_PATH)

        print("Index created and saved.")

    return vectorstore