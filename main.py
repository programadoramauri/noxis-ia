from llm.local_llm import load_llm

llm = load_llm()
response = llm.invoke("O que é inteligência artificial?")
print(response)
