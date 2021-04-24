from unittest import TestCase

from rosie.chatbot import Chatbot


class TestChatbot(TestCase):
    def setUp(self):
        self.chatbot = Chatbot("test")

    def test_has_all_attributes(self):
        self.assertEqual(
            hasattr(self.chatbot, "intents"),
            True,
            "Chatbot: no intents attribute found",
        )
        self.assertEqual(
            hasattr(self.chatbot, "name"),
            True,
            "Chatbot: no name attribute found",
        )

    def test_has_all_methods(self):
        self.assertEqual(
            hasattr(self.chatbot, "add_intent"),
            True,
            "Chatbot: no add_intent method found",
        )

        add_intent = self.chatbot.add_intent
        self.assertEqual(
            hasattr(add_intent, "__call__"),
            True,
            "Chatbot: add_intent is not a method",
        )

        self.assertEqual(
            add_intent.__code__.co_argcount,
            1 + 2,
            "Chatbot: add_intent should accept two parameters (name, phrases)",
        )

    def test_correctly_adds_new_intent(self):
        intent_name = "test_intent"
        intent_phrases = ["test1", "test2", "test3"]
        self.assertEqual(
            self.chatbot.intents.get(intent_name),
            None,
            "Chatbot: intents should be empty when initialized",
        )
        self.chatbot.add_intent(intent_name, intent_phrases)
        self.assertEqual(
            self.chatbot.intents.get(intent_name),
            intent_phrases,
            "Chatbot: add_intents failed to add to intents",
        )

    def test_can_initiate_correctly(self):
        chatbot = Chatbot("test_name")
        self.assertEqual(
            chatbot.name,
            "test_name",
            "Chatbot: name attribute initialized incorrectly",
        )
