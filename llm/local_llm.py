from langchain_community.llms import LlamaCpp
from config import Config


def load_llm():
    return LlamaCpp(
        model_path=Config.LLM_PATH,
        n_ctx=2048,
        n_gpu_layers=0,
        temperature=0.3,
    )
