from chatbot import create_chatbot

def main():
    chat = create_chatbot()
    print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
    chat.converse()

if __name__ == "__main__":
    main()
