import tkinter as tk
from tkinter import scrolledtext


responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am a simple chatbot created using Python.",
    "bye": "Goodbye! Have a great day!",
}

# Define a function to get the bot's response
def get_response(user_input):
    # Convert the input to lowercase to make the bot case-insensitive
    user_input = user_input.lower()
    
    # Find the response in the predefined dictionary
    return responses.get(user_input, "I'm sorry, I don't understand that.")

# Function to handle sending messages
def send_message():
    user_input = user_input_entry.get()
    if user_input:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        chat_log.config(state=tk.DISABLED)
        user_input_entry.delete(0, tk.END)
        
        response = get_response(user_input)
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "Chatbot: " + response + "\n")
        chat_log.config(state=tk.DISABLED)
        
        # Automatically scroll to the bottom
        chat_log.yview(tk.END)
        
        if user_input.lower() == "bye":
            root.quit()

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Create a scrolled text widget for chat log
chat_log = scrolledtext.ScrolledText(root, state='disabled', wrap='word', width=50, height=20)
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create an entry widget for user input
user_input_entry = tk.Entry(root, width=40)
user_input_entry.grid(row=1, column=0, padx=10, pady=10)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Initialize the chat log with a welcome message
chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, "Chatbot: Hello! Type 'bye' to exit.\n")
chat_log.config(state=tk.DISABLED)

# Run the main loop
root.mainloop()

