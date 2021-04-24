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
        "oi",
        "olá",
        "tudo bem",
        "como vai",
        "opa",
        "bom dia",
        "boa noite",
        "boa tarde",
    ],
)


print(chatbot.get_intent_by_token("quero saber o preço"))
