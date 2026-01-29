import chromadb
from sentence_transformers import SentenceTransformer
import uuid

class VectorStore:
    def __init__(self, collection_name="kos", persist_dir=".chroma"):
        self.client = chromadb.Client(
            settings=chromadb.Settings(
                persist_directory=persist_dir
            )
        )
        self.encoder = SentenceTransformer("all-MiniLM-L6-v2")
        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(self, docs):
        if not docs:
            raise ValueError("No documents to add")

        embeddings = self.encoder.encode(docs).tolist()
        ids = [str(uuid.uuid4()) for _ in docs]

        self.collection.add(
            documents=docs,
            embeddings=embeddings,
            ids=ids
        )

    def search(self, query, k=3):
        q_emb = self.encoder.encode([query]).tolist()
        return self.collection.query(
            query_embeddings=q_emb,
            n_results=k
        )
