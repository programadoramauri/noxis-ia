import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    LLM_MODEL = "mistral-7b-instruct-v0.2.Q4_K_M.gguf"
    LLM_FILE = "mistral-7b-instruct-v0.2.Q4_K_M.gguf"
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    LLM_PATH = os.path.join(BASE_DIR, "models", LLM_FILE)
