from langchain_community.embeddings import vertexai
from config import Config
from llm.local_llm import load_llm
from rag.vector_store import VectorStore
from core.query_router import QueryRouter
from core.chain_builder import ChainBuilder
from plugins.plugin_manager import PluginManager
import time


def main():
    print(f"Iniciando sistema com modelo: {Config.LLM_FILE}")
    print(f"Bqnco de dados vetorial: {Config.CHROMA_DB_PATH}")

    plugin_manager = PluginManager()
    router = QueryRouter()
    vector_store = VectorStore()
    retriever = vector_store.as_retriever()
    rag_chain = ChainBuilder.build_rag_chain(retriever)
    llm = load_llm()

    while True:
        try:
            query = input("Você: ")
            if query.lower() in ["sair", "exit", "quit"]:
                break

            start_time = time.time()

            query_type = router.route(query)
            print(f"Tipo de consulta detectado: {query_type}")

            if query_type == "calculation":
                plugin = plugin_manager.get_handler(query)
                response = (
                    plugin.handle(query) if plugin else "Nenhum plugin disponível"
                )
                print(f"[Plugin] {response}")
            elif query_type == "document retrieval":
                result = rag_chain.invoke({"query": query})
                response = result = result["result"]
                sources = "\n".join(
                    set(doc.metadata["source"] for doc in result["source_documents"])
                )
                print(f"[RAG] {response}")
                print(f"Fontes: {sources}")
            else:
                response = llm.invoke(query)
                print(f"[LLM] {response}")

            elapsed = time.time() - start_time
            print(f"Tempo de resposta: {elapsed: .2f}s")

        except Exception as e:
            print(f"Erro: {str(e)}")
            import traceback

            traceback.print_exc()


if __name__ == "__main__":
    main()
