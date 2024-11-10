from langchain_ollama import OllamaLLM
# from langchain_core.prompts import ChatpromptTemp


while 1:
    model = OllamaLLM(model="llama3.2:1b")
    userinp = input("Please enter your question: ")
    result = model.invoke(input=userinp)
    print(result) 