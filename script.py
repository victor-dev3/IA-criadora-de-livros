from langchain_ollama import OllamaLLM

modelo = OllamaLLM(model="llama3.2")
resposta = modelo.invoke("Comece a me ajudar.")
print(resposta)