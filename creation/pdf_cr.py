# Install library first (run once)
# !pip install fpdf

from fpdf import FPDF
import os

# Create folder
os.makedirs("../data/pdf_files", exist_ok=True)

# PDF content
pdf_contents = {
    "rag_basics.pdf": """
RAG Basics

RAG stands for Retrieval-Augmented Generation.

RAG combines:
1. Retrieval System
2. Large Language Model

Workflow:
- User asks a question
- Relevant documents are retrieved
- Context is passed to the LLM
- LLM generates an answer

Benefits:
- Better accuracy
- Reduced hallucinations
- Uses custom data
""",

    "vector_database_intro.pdf": """
Vector Database Introduction

A vector database stores embeddings.

Embeddings are numerical representations of text.

Popular Vector Databases:
- FAISS
- ChromaDB
- Pinecone
- Weaviate

Why use vector databases?
- Fast similarity search
- Semantic search
- Efficient retrieval
""",

    "langchain_rag_pipeline.pdf": """
LangChain RAG Pipeline

Main Components:
1. Document Loader
2. Text Splitter
3. Embedding Model
4. Vector Store
5. Retriever
6. LLM

Example Workflow:
- Load PDFs
- Split text into chunks
- Create embeddings
- Store embeddings
- Retrieve relevant chunks
- Generate answer
"""
}

# Function to create PDF
def create_pdf(filename, content):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    for line in content.strip().split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(f"../data/pdf_files/{filename}")

# Generate PDFs
for filename, content in pdf_contents.items():
    create_pdf(filename, content)

print("PDF files generated successfully!")