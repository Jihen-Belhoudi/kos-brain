from .vector_store import VectorStore
from core.llm_client import LLMClient

class RAGBrain:
    def __init__(self):
        self.store = VectorStore()
        self.llm = LLMClient(model="mistral")

    def ingest(self, docs):
        if not docs:
            raise ValueError("No documents to ingest")
        self.store.add_documents(docs)

    def query(self, question):
        results = self.store.search(question)

        if not results or "documents" not in results:
            return "No relevant documents found."

        docs = results["documents"][0]
        context = "\n\n".join(docs)

        prompt = f"""
You are a helpful assistant.
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""

        return self.llm.generate(prompt)
