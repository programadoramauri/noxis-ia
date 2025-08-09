from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from llm.local_llm import load_llm

PROMPT_TEMPLATE = """<s>[INST] Você é um assistente útil. Responda à pergunta baseando-se apenas no contexto fornecido:
Responda APENAS em português

Contexto:
{context}

Pergunta: {question} [/INST]
"""


class ChainBuilder:
    @staticmethod
    def build_rag_chain(retriever):
        llm = load_llm()
        prompt = PromptTemplate(
            template=PROMPT_TEMPLATE, input_variables=["context", "question"]
        )
        return RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True,
        )
