# config.py

# Path to store PDF documents
PDF_STORAGE_PATH = "document_store/pdfs/"

# Prompt template for the Q/A agent
PROMPT_TEMPLATE = """
You are an expert research assistant. Use the provided context to answer the query.
If unsure, state that you don't know. Be concise and factual (max 3 sentences).

Query: {user_query}
Context: {document_context}
Answer:
"""

# Import and configure models (Ollama-based in this example)
from langchain_ollama import OllamaEmbeddings, OllamaLLM

# Create an embedding model for our vector store
EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:7b")
# Create a language model to generate answers
LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:7b")

# Create an in-memory vector store for document chunks
from langchain_core.vectorstores import InMemoryVectorStore
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
