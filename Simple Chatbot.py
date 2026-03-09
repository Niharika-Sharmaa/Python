while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hello!")
    elif "how are you" in user:
        print("Bot: I am fine.")
    elif "bye" in user:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")
