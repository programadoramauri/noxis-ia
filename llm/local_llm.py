from langchain_community.llms import LlamaCpp
from config import Config


def load_llm():
    return LlamaCpp(
        model_path=Config.LLM_PATH,
        n_ctx=2048,
        n_gpu_layers=0,
        n_threads=10,
        n_threads_batch=10,
        n_batch=512,
        temperature=0.2,
        max_tokens=512,
        verbose=True,
        streaming=True,
        use_mlock=True,
        seed=42,
        use_map=True,
        low_vram=False,
        offload_kqv=True,
        mul_mat_q=False,
        lora_base=None,
        rope_freq_base=10000,
        rope_freq_scale=1,
        model_kwargs={"vocab_only": False},
    )
