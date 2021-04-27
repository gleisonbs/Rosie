from flask import request
from flask_restful import Resource

from config.db import db
from serializers.chatbot_serializer import ChatbotSchema


class Chatbot(Resource):
    def get(self):
        return "Hello", 200

    def post(self):
        cs = ChatbotSchema()
        chatbot = cs.load(request.json)
        db.session.add(chatbot)
        db.session.commit()
        response = cs.jsonify(chatbot)
        response.status_code = 201
        return response
