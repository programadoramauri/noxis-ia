from langchain_chroma import Chroma
from rag.embeddings import get_embeddings
from config import Config


class VectorStore:
    def __init__(self):
        self.embeddings = get_embeddings()
        self.client = Chroma(
            persist_directory=Config.CHROMA_DB_PATH,
            embedding_function=self.embeddings,
            collection_name=Config.CHROMA_COLLECTION,
        )

    def as_retriever(self, k=5):
        return self.client.as_retriever(search_kwargs={"k": k})
