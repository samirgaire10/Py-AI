import ollama
from langchain_ollama import OllamaLLM
from tkinter import *

window = Tk()
window.geometry("700x500")
window.title("PyAI Assistant")
window.config(background="skyblue")

# Function to get the AI response
def get_response():
    userinp = user_input.get()
    
    # Set up the Ollama model
    model = OllamaLLM(model="llama3.2:1b")
    result = model.invoke(input=userinp)
    
    response_text.config(state=NORMAL)
    response_text.delete(1.0, END)  
    response_text.insert(END, "AI: " + result)
    response_text.config(state=DISABLED)


header_label = Label(window, text="Welcome to PyAI", font=("Arial", 18, "bold"), bg="skyblue", fg="white")
header_label.pack(pady=20)

instruction_label = Label(window, text="Please enter your question below:", font=("Arial", 14), bg="skyblue")
instruction_label.pack(pady=10)

user_input_frame = Frame(window, bg="skyblue")
user_input_frame.pack(pady=10)

user_input = Entry(user_input_frame, font=("Arial", 14), width=40, relief=SOLID, bd=2)
user_input.pack(side=LEFT, padx=5)

send_button = Button(user_input_frame, text="Send", font=("Arial", 14), command=get_response, bg="blue", fg="white", relief=RAISED, bd=2)
send_button.pack(side=RIGHT, padx=5)

response_frame = Frame(window, bg="skyblue")
response_frame.pack(pady=20)

response_text = Text(response_frame, font=("Arial", 14), height=10, width=55, wrap=WORD, bg="white", relief=SOLID, bd=2)
response_text.pack()
response_text.config(state=DISABLED)

window.mainloop()
