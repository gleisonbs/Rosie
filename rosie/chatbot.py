from rosie.nlp_engine import NLPEngine


class Chatbot:
    def __init__(self, name):
        self.name = name
        self.intents = {}
        self.nlp = NLPEngine().pt

    def add_intent(self, name, phrases):
        self.intents[name] = phrases

    def get_intent_by_token(self, token):
        similarities = {}
        largest = 0
        for intent, phrases in self.intents.items():
            max_intent_similarity = max(
                [token.similarity(self.nlp(p)) for p in phrases]
            )
            similarities[max_intent_similarity] = intent
            largest = max(largest, max_intent_similarity)
        return similarities[largest]

    def __str__(self):
        if len(self.intents) == 0:
            return "{}"

        response = ""
        for intent, phrases in self.intents.items():
            response += f"intent:{intent}\n"
            response += "".join([f" - {phrase}\n" for phrase in phrases])
        return response
