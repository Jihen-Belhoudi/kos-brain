from rag.doc_loader import load_docs
from rag.rag_engine import RAGBrain
import sys
import os
import traceback

def main():
    print("cwd:", os.getcwd())
    print("sys.path:")
    for p in sys.path:
        print(" ", p)
    try:
        print("Loading documents...")
        docs = load_docs("data")

        brain = RAGBrain()
        print("Ingesting...")
        brain.ingest(docs)

        print("Querying...")
        answer = brain.query("What is this document about?")
        print(answer)
    except Exception as e:
        print("Exception raised:", type(e).__name__)
        traceback.print_exc()

if __name__ == "__main__":
    main() 
