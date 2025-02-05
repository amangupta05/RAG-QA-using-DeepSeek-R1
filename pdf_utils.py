# pdf_utils.py

import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import PDF_STORAGE_PATH

def save_uploaded_file(uploaded_file):
    """
    Save the uploaded file to the designated PDF storage path.
    """
    os.makedirs(PDF_STORAGE_PATH, exist_ok=True)
    file_path = os.path.join(PDF_STORAGE_PATH, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def load_pdf_documents(file_path):
    """
    Load PDF documents using PDFPlumberLoader.
    """
    loader = PDFPlumberLoader(file_path)
    return loader.load()

def chunk_documents(raw_documents, chunk_size=1000, chunk_overlap=200):
    """
    Split the raw documents into smaller text chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True
    )
    return splitter.split_documents(raw_documents)
