from flask_restful import Resource, reqparse

from models.chatbot_model import ChatbotModel


class Chatbot(Resource):
    def get(self, name):
        chatbot = ChatbotModel.get_by_name(name)
        return chatbot.json(), 200


class ChatbotList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name", type=str, required=True, help="This field is mandatory"
    )

    def get(self):
        chatbots = ChatbotModel.get_all()
        return {"chatbots": [c.json() for c in chatbots]}, 200

    def post(self):
        data = ChatbotList.parser.parse_args()
        chatbot = ChatbotModel(name=data["name"])
        chatbot.save()
        return chatbot.json(), 201
