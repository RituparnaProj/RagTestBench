A modular Retrieval-Augmented Generation (RAG) evaluation framework built using a fully local LLM stack.

This project demonstrates how to:

Build a RAG pipeline
Evaluate LLM responses
Add validation layers for GenAI systems
Test chatbot answers using semantic similarity + LLM judge
The framework is designed as a reference architecture for GenAI testing and validation.

Architecture:
User Question
      ↓
Guardrails Layer
      ↓
RAG Pipeline
      ↓
Load Documents
      ↓
Create Vector Store (FAISS)
      ↓
Retrieve Context
      ↓
Generate Answer (Ollama LLM)
      ↓
Evaluation Layer
      ↓
Semantic Similarity Validator
      +
LLM Judge
      ↓
Final Score


Tech Stack
Python 3
LangChain
Ollama (Local LLM runtime)
FAISS (Vector database)
lama3 (LLM model via Ollama)
nomic-embed-text (Embedding model via Ollama)
This framework runs fully locally without any external APIs.

Project Structure:
 ContextFramework/

├── dataset/
│   └── golden_dataset.json
│
├── rag/
│   ├── embedder.py
│   ├── generator.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   └── vector_store.py
│
├── validator/
│   └── similarity_validator.py
│
├── ragas_eval/
│   └── ragas_score.py
│
├── llm_judge/
│   └── judge.py
│
├── guardrails/
│   └── guardrail.py
│
├── run_tests.py
│
└── README.md


Setup Instructions:
1.Install Python Dependencies - pip install langchain langchain-community faiss-cpu
2.Install Ollama - Download Ollama from:
https://ollama.com
Start the Ollama server:
3.Pull Required Models
ollama pull llama3
ollama pull nomic-embed-text
4.Run the Framework
python run_tests.py

What This Framework Evaluates:
The framework evaluates chatbot responses using multiple validation layers.
1 Semantic Similarity
Compares expected answer vs generated answer using embedding similarity.
2 LLM Judge
Uses another LLM to score correctness of the response.
3 Final Score
A weighted score combining:
Final Score =
0.6 * Similarity Score
+
0.4 * LLM Judge Score

Example Output:
Question: What is the capital of France?

Actual Answer: Paris

Scores:
similarity_score: 0.91
judge_score: 0.87
final_score: 0.89

Purpose of This Project:
This framework is designed as:
A reference implementation for RAG testing
A learning project for GenAI validation
A foundation for building advanced LLM evaluation pipelines
It demonstrates how to build testable AI systems instead of only generating responses.

Future Improvements
Planned improvements include:
Add structured logging
Add CI/CD pipeline
Support multiple datasets
Add latency and performance metrics
Improve prompt engineering
Upgrade embeddings to the latest langchain-ollama package

Author
Built as part of continuous learning in:
GenAI Testing
RAG Systems
LLM Evaluation Frameworks