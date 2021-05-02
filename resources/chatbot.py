from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse

from models.chatbot_model import ChatbotModel


def unauthorized():
    return {"message": "Unauthorized"}, 401


def forbidden():
    return {"message": "Forbidden"}, 403


def is_authenticated(decoded_token, user_id):
    return decoded_token.get("user_id", 0) != 0


def has_permission(decoded_token, user_id):
    return decoded_token.get("user_id", 0) == user_id


class Chatbot(Resource):
    def get(self, name):
        chatbot = ChatbotModel.get_by_name(name)
        return chatbot.json(), 200


class ChatbotList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name", type=str, required=True, help="This field is mandatory"
    )

    @jwt_required()
    def get(self, user_id):
        jwt_payload = get_jwt_identity()
        if not is_authenticated(jwt_payload, user_id):
            return unauthorized()

        if not has_permission(jwt_payload, user_id):
            return forbidden()

        chatbots = ChatbotModel.get_all(user_id)
        return {"chatbots": [c.json() for c in chatbots]}, 200

    @jwt_required()
    def post(self, user_id):
        jwt_payload = get_jwt_identity()
        if not is_authenticated(jwt_payload, user_id):
            return unauthorized()

        if not has_permission(jwt_payload, user_id):
            return forbidden()

        data = ChatbotList.parser.parse_args()
        chatbot = ChatbotModel(user_id=user_id, name=data["name"])
        chatbot.save()
        return chatbot.json(), 201
