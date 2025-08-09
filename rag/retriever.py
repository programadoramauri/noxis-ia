from langchain_community.vectorstores import Chroma


class Retriever:
    def __init__(self, vector_store):
        self.retriever = vector_store.langchain_chroma.as_retriever()

    def get_relevant_documents(self, query: str) -> list:
        return self.retriever.get_relevant_documents(query)
