from unittest import TestCase
from rosie.chatbot import Chatbot

class TestChatbot(TestCase):
  def setUp(self):
    self.chatbot = Chatbot("test")

  def test_has_all_attributes(self):
    self.assertEqual(hasattr(self.chatbot, "intents"), True,
      "Chatbot: no intents attribute found")
    self.assertEqual(hasattr(self.chatbot, "name"), True,
      "Chatbot: no name attribute found")

  def test_can_initiate_correctly(self):
    chatbot = Chatbot("test_name")
    self.assertEqual(chatbot.name, "test_name", 
      "Chatbot: name attribute incorrectly initialized")