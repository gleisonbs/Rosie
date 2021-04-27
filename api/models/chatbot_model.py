from api.db import db


class Chatbot(db.Model):
    __tablename__ = "chatbot"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
