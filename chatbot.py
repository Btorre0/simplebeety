import nltk
from nltk.chat.util import Chat, reflections
from pairs import pairs

# Download NLTK data (only needed once)
nltk.download('punkt')

def create_chatbot():
    """
    Creates and returns a Chatbot instance using the defined pairs and reflections.
    """
    return Chat(pairs, reflections)