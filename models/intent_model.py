from config.db import db


class IntentModel(db.Model):
    __tablename__ = "intents"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    chatbot_id = db.Column(db.Integer, db.ForeignKey("chatbots.id"))
    chatbot = db.relationship("ChatbotModel")

    def __init__(self, name, chatbot_id):
        self.name = name
        self.chatbot_id = chatbot_id

    def json(self):
        return {"id": self.id, "name": self.name}

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_chatbot_id(cls, chatbot_id):
        return cls.query.filter_by(chatbot_id=chatbot_id).all()

    def save(self):
        db.session.add(self)
        db.session.commit()
