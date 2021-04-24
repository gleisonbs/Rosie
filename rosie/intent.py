class Intent:
    def __init__(self, nlp_engine, name, phrases=[]):
        self.nlp_engine = nlp_engine
        self.name = name
        self.phrases = set([nlp_engine(phrase) for phrase in phrases])

    def get_similarity(self, token):
        token = self.nlp_engine(token)
        return max([token.similarity(phrase) for phrase in self.phrases])

    def add_phrase(self, phrase):
        self.phrases.add(self.nlp_engine(phrase))

    def __str__(self):
        if len(self.phrases) == 0:
            return f"intent:{self.name}\n no phrases defined"

        sorted_phrases = sorted(list(self.phrases), key=lambda x: str(x))
        response = f"intent:{self.name}\n"
        response += "".join([f" - {phrase}\n" for phrase in sorted_phrases])
        return response
