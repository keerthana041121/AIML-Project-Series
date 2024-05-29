# Define a dictionary of predefined responses
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

# Main chat loop
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if the user wants to exit
        if user_input.lower() == "bye":
            print("Chatbot: " + responses["bye"])
            break
        
        # Get the bot's response and print it
        response = get_response(user_input)
        print("Chatbot: " + response)

# Run the chatbot
if __name__ == "__main__":
    chat()
