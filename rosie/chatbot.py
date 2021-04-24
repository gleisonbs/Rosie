class Chatbot:
  def __init__(self, name):
    self.name = name
    self.intents = {}

  def add_intent(self, name, phrases):
    self.intents[name] = phrases