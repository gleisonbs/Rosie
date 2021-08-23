from rosie.intent import Intent


class Chatbot:
    def __init__(self, nlp_engine, name):
        self.name = name
        self.intents = []
        self.nlp_engine = nlp_engine

    def add_intent(self, name, phrases):
        self.intents.append(
            Intent(self.nlp_engine, name, [p.lower() for p in phrases])
        )

    def get_intent_by_token(self, token):
        value = 0
        name = ""
        token = token.lower()
        for intent in self.intents:
            similarity = intent.get_similarity(token)
            if similarity > value:
                value, name = similarity, intent.name
        return name, value

    def __str__(self):
        if len(self.intents) == 0:
            return "{}"
        return "".join([str(i) for i in self.intents])
