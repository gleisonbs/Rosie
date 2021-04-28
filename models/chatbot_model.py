from config.db import db


class ChatbotModel(db.Model):
    __tablename__ = "chatbots"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    intents = db.relationship("IntentModel", lazy="dynamic")

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "intents": [i.json() for i in self.intents.all()],
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
