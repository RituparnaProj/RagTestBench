from rag.vector_store import create_vectorstore
from rag_pipeline import load_documents

def build_index():

    docs = load_documents()

    vectorstore = create_vectorstore(docs)

    vectorstore.save_local("faiss_index")

    print("Index created and saved!")

if __name__ == "__main__":
    build_index()