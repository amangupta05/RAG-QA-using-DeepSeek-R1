# qa_agent.py

from config import PROMPT_TEMPLATE, DOCUMENT_VECTOR_DB, LANGUAGE_MODEL
from langchain_core.prompts import ChatPromptTemplate

def index_documents(document_chunks):
    """
    Add document chunks to the vector store.
    """
    DOCUMENT_VECTOR_DB.add_documents(document_chunks)

def find_related_documents(query):
    """
    Retrieve documents related to the query from the vector store.
    """
    return DOCUMENT_VECTOR_DB.similarity_search(query)

def generate_answer(user_query, context_documents):
    """
    Generate an answer by combining the retrieved context and the user query.
    Uses a prompt template and the language model.
    
    (Optionally, you can wrap this chain inside a LangGraph workflow.)
    """
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    # In this simple chain, we pipe the prompt into the language model.
    response_chain = conversation_prompt | LANGUAGE_MODEL
    return response_chain.invoke({"user_query": user_query, "document_context": context_text})
