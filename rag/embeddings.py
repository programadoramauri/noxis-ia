from langchain_huggingface import HuggingFaceEmbeddings
from config import Config


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=Config.EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
