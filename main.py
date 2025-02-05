# main.py

import streamlit as st
from config import *
from pdf_utils import save_uploaded_file, load_pdf_documents, chunk_documents
from qa_agent import index_documents, find_related_documents, generate_answer

# ----------------- Custom CSS Styling ----------------- #
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    
    /* Chat Input Styling */
    .stChatInput input {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border: 1px solid #3A3A3A !important;
    }
    
    /* Chat Message Styling */
    .stChatMessage[data-testid="stChatMessage"] {
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #1E1E1E !important;
        border: 1px solid #3A3A3A !important;
    }
    
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
        background-color: #2A2A2A !important;
        border: 1px solid #404040 !important;
    }
    
    .stFileUploader {
        background-color: #1E1E1E;
        border: 1px solid #3A3A3A;
        border-radius: 5px;
        padding: 15px;
    }
    
    h1, h2, h3 {
        color: #00FFAA !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------- UI Header ----------------- #
st.title("📘 RAG-QA-using-DeepSeek-R1")
st.markdown("### Intelligent Document Assistant with Web-based Q/A")
st.markdown("---")

# ----------------- File Upload ----------------- #
uploaded_pdf = st.file_uploader(
    "Upload Research Document (PDF)",
    type="pdf",
    help="Select a PDF document for analysis",
    accept_multiple_files=False
)

if uploaded_pdf:
    # Save the uploaded PDF
    saved_path = save_uploaded_file(uploaded_pdf)
    # Load and process the PDF
    raw_docs = load_pdf_documents(saved_path)
    doc_chunks = chunk_documents(raw_docs)
    # Index the document chunks for retrieval
    index_documents(doc_chunks)
    
    st.success("✅ Document processed and indexed successfully!")
    
    # ----------------- Q/A Chat Interface ----------------- #
    user_query = st.chat_input("Enter your question about the document...")
    if user_query:
        with st.chat_message("user"):
            st.write(user_query)
        with st.spinner("Analyzing document..."):
            # Retrieve relevant chunks and generate an answer
            relevant_docs = find_related_documents(user_query)
            answer = generate_answer(user_query, relevant_docs)
        with st.chat_message("assistant", avatar="🤖"):
            st.write(answer)
