def chatbox_response(user_choice):
    user_choice = user_choice.lower()

    if "hello" in user_choice or "hi" in user_choice:
        return "Hello! How can I help you today?"

    elif "how are you" in user_choice:
        return "I'm doing great, thanks for asking!"

    elif "your name" in user_choice:
        return "I'm a basic Python chatbot created by you."

    elif "bye" in user_choice:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I didn't understand that."


print("Welcome to our chatbot")
print("Chatbot: Hello! Type something (type 'bye' to exit)")

while True:
    user = input("You: ")
    response = chatbox_response(user)

    print("Chatbot:", response)

    if "bye" in user.lower():
        break