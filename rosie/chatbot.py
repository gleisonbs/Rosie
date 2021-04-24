class Chatbot:
    def __init__(self, name):
        self.name = name
        self.intents = {}

    def add_intent(self, name, phrases):
        self.intents[name] = phrases

    def __str__(self):
        if len(self.intents) == 0:
            return "{}"

        response = ""
        for k, v in self.intents.items():
            response += f"intent:{k}\n"
            response += "".join([f" - {p}\n" for p in v])
        return response
