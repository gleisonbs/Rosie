# import spacy
from rosie.chatbot import Chatbot

chatbot = Chatbot("Pizzaria")

chatbot.add_intent(
    "price", ["qual o valor", "quanto custa", "preço", "me fala o total"]
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

print(chatbot)

# nlp = spacy.load("pt_core_news_lg")
# question = nlp("qual o preço?")
# for phrase in phrases:
#     print(nlp(phrase).similarity(question))
