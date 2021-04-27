from rosie.chatbot import Chatbot
from rosie.nlp_engine import NLPEngine

chatbot = Chatbot(NLPEngine().pt, "Pizzaria")

chatbot.add_intent(
    "price",
    ["qual o valor", "quanto custa", "preço", "me fala o total", "comprar"],
)

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

chatbot.add_intent(
    "soda",
    [
        "tem coca cola" "refrigerantes",
        "que refris vocês tem",
        "tem refrigerante 2l",
        "quais as opções de refrigerantes",
    ],
)


print(chatbot.get_intent_by_token("tem coca de 2l"))
