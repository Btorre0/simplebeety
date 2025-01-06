import unittest
from chatbot import create_chatbot
from nltk.chat.util import Chat

class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.chatbot = create_chatbot()

    def test_chatbot_instance(self):
        self.assertIsNotNone(self.chatbot)
        self.assertIsInstance(self.chatbot, Chat)

    def test_chatbot_response(self):
        input_statement = "Hello"
        response = self.chatbot.respond(input_statement)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)

    def test_chatbot_greeting(self):
        input_statement = "Hi"
        response = self.chatbot.respond(input_statement)
        self.assertIn(response, ["Hello", "Hi there", "Greetings"])

    def test_chatbot_farewell(self):
        input_statement = "Goodbye"
        response = self.chatbot.respond(input_statement)
        self.assertIn(response, ["Goodbye", "See you later", "Bye"])

    def test_chatbot_unknown(self):
        input_statement = "What is the meaning of life?"
        response = self.chatbot.respond(input_statement)
        self.assertIn(response, ["I don't know", "Can you rephrase that?", "I'm not sure"])

if __name__ == '__main__':
    unittest.main()