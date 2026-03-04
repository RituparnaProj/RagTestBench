# RAG Evaluation Framework (Local Ollama Stack)

A modular Retrieval-Augmented Generation (RAG) evaluation framework built using:

- LangChain
- Ollama (local LLM + embeddings)
- FAISS vector store
- Guardrails layer
- RAG evaluation (similarity + LLM judge)

This project demonstrates how to build and evaluate a local RAG pipeline in a structured, testable way.

---

## Architecture

User Question  
→ Guardrails  
→ RAG Pipeline  
  → Load Documents  
  → Create Vector Store (FAISS)  
  → Retrieve Context  
  → Generate Answer (Ollama LLM)  
→ Evaluation Layer  
  → Similarity Score  
  → LLM Judge Score  
  → Final Score  

---

## Tech Stack

- Python 3.x
- LangChain
- Ollama
- FAISS
- Nomic Embed Text (Ollama embedding model)
- Llama3 (Ollama LLM)

---

---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies

```bash
pip install langchain langchain-community faiss-cpu

---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies

```bash
pip install langchain langchain-community faiss-cpu
2️⃣ Install Ollama

Download from:
https://ollama.com

Start server:

ollama serve
3️⃣ Pull Required Models
ollama pull llama3
ollama pull nomic-embed-text

4️⃣ Run the Test Framework
python run_tests.py

📊 What This Framework Evaluates

Whether retrieved context is relevant

Whether generated answer matches expected answer

How similar the answer is semantically

Whether LLM judge approves the response

Final score is a weighted combination of similarity + judge score.

🎯 Purpose

This project is intended as:

A reference implementation of a local RAG evaluation framework

A learning foundation for GenAI testing and validation

A base architecture that can be extended with CI/CD, logging, metrics, and dataset scaling

🔮 Future Improvements

Add structured logging

Add CI pipeline

Add multiple test datasets

Add performance metrics (latency tracking)

Improve prompt engineering

Replace deprecated embeddings class

👩‍💻 Author

Built as part of continuous learning in GenAI test automation and RAG system validation.


---