1. uv python install 3.11
2. uv venv
3. source .venv/bin/activate
4. uv pip install ipykernel
5. python -m ipykernel install --user --name=rag-311 --display-name "Python (RAG 3.11)"
6. uv add -r requirements.txt