## cretae a simple txt file
import os
os.makedirs("../data/text_files", exist_ok = True)

sample_texts = {
    "../data/text_files/python_intro.txt": """
Python is a popular high-level programming language known for its simplicity and readability.

Key features of Python:
1. Easy to learn and use
2. Large standard library
3. Supports object-oriented programming
4. Widely used in AI, Machine Learning, and Web Development

Example of a simple Python program:

def greet(name):
    return f"Hello, {name}"

print(greet("World"))

Python is commonly used for:
- Data Science
- Automation
- Web Applications
- Artificial Intelligence
- Backend Development
RAG stands for Retrieval-Augmented Generation.

RAG combines:
1. Information Retrieval
2. Large Language Models (LLMs)

How RAG works:
- User asks a question
- Relevant documents are retrieved from a database
- Retrieved context is sent to the LLM
- LLM generates an accurate response using the context

Main components of a RAG pipeline:
1. Document Loader
2. Text Splitter
3. Embedding Model
4. Vector Database
5. Retriever
6. Language Model

Benefits of RAG:
- Reduces hallucinations
- Uses private/custom data
- Improves answer accuracy
- Keeps LLM responses up to date

Popular tools used in RAG:
- LangChain
- FAISS
- ChromaDB
- OpenAI Embeddings
- Hugging Face Models
"""
}

for filepath, content in sample_texts.items():
    with open(filepath, 'w', encoding = "utf-8") as f:
        f.write(content)
print("DOne!")