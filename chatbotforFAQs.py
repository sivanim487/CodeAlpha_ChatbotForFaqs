print("=== FAQ Chatbot ===")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "what is your name":
        print("Bot: I am a FAQ Chatbot.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "who developed python":
        print("Bot: Python was developed by Guido van Rossum.")

    elif user == "what is codealpha":
        print("Bot: CodeAlpha provides internship opportunities and projects.")

    elif user == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")