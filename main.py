import ollama
from langchain_ollama import OllamaLLM
from tkinter import *

window = Tk()
window.geometry("700x700")
window.title("PyAI")
window.config(background="skyblue")

def get_response():
    userinp = user_input.get()
    
    model = OllamaLLM(model="llama3.2:1b")
    result = model.invoke(input=userinp)
    
    response_label.config(text="AI: " + result)

instruction_label = Label(window, text="Please enter your question:", font=("Arial", 14), bg="skyblue")
instruction_label.pack(pady=10)



Send_button = Button(window, text="Send", font=("Arial", 14), command=get_response)
Send_button.pack(side=RIGHT ,pady=10)

response_label = Label(window, text="Response: ", font=("Arial", 14), bg="skyblue")
response_label.pack(pady=10)

user_input = Entry(window, font=("Arial", 14), width=40)
user_input.pack(side=LEFT, pady=10)

window.mainloop()
