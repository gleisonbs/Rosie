import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rosie.chatbot import Chatbot
from rosie.nlp_engine import NLPEngine

# Create the chatbot with the name "Pizzaria"
chatbot = Chatbot(NLPEngine().pt, "Pizzaria")

# Add the price intent
chatbot.add_intent(
    "price",
    ["qual o valor", "quanto custa", "preço", "me fala o total", "comprar"],
)

# Add the greetings intent
chatbot.add_intent(
    "greet",
    [
        "e aí" "oi",
        "olá",
        "tudo bem",
        "como vai",
        "opa",
        "bom dia",
        "boa noite",
        "boa tarde",
    ],
)

# Add the soda intent
chatbot.add_intent(
    "soda",
    [
        "tem coca cola",
        "refrigerantes",
        "que refris vocês tem",
        "tem refrigerante 2l",
        "quais as opções de refrigerantes",
    ],
)

# Try to guess the intent by the phrase
print(chatbot.get_intent_by_token("tem coca de 2l"))
