import tempfile
import os
from langchain_community.document_loaders import PyPDFLoader

def process_pdfs(pdf_files):
    """Process uploaded PDF files into text chunks."""
    documents = []
    for pdf_file in pdf_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(pdf_file.getvalue())
            temp_file_path = temp_file.name

        loader = PyPDFLoader(temp_file_path)
        pages = loader.load_and_split()
        documents.extend(pages)
        os.remove(temp_file_path)

    return documents
