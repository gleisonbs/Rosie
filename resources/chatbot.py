from flask_restful import Resource, reqparse

from models.chatbot_model import ChatbotModel


class Chatbot(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name", type=str, required=True, help="This field is mandatory"
    )

    def get(self):
        chatbots = ChatbotModel.get_all()
        print(chatbots)
        return {"chatbots": [c.json() for c in chatbots]}, 200

    def post(self):
        data = Chatbot.parser.parse_args()
        chatbot = ChatbotModel(**data)
        chatbot.save()
        return chatbot.json(), 201
