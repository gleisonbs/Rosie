from rosie.intent import Intent


class Chatbot:
    def __init__(self, nlp_engine, name):
        self.name = name
        self.intents = []
        self.nlp_engine = nlp_engine

    def add_intent(self, name, phrases):
        self.intents.append(Intent(self.nlp_engine, name, phrases))

    def get_intent_by_token(self, token):
        max_similiraty_value = 0
        max_similiraty_name = ""
        for intent in self.intents:
            similarity = intent.get_similarity(token)
            if similarity > max_similiraty_value:
                max_similiraty_value = similarity
                max_similiraty_name = intent.name
        return max_similiraty_name, max_similiraty_value

    def __str__(self):
        if len(self.intents) == 0:
            return "{}"
        return "".join([str(i) for i in self.intents])
