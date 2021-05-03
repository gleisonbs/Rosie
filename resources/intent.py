from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse

from models.intent_model import IntentModel


def unauthorized():
    return {"message": "Unauthorized"}, 401


def forbidden():
    return {"message": "Forbidden"}, 403


def is_authenticated(decoded_token, user_id):
    return decoded_token.get("user_id", 0) != 0


def has_permission(decoded_token, user_id):
    return decoded_token.get("user_id", 0) == user_id


class Intent(Resource):
    def get(self, name):
        intent = IntentModel.get_by_name(name)
        return intent.json(), 200


class IntentList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name", type=str, required=True, help="This field is mandatory"
    )

    @jwt_required()
    def get(self, user_id, chatbot_id):
        jwt_payload = get_jwt_identity()
        if not is_authenticated(jwt_payload, user_id):
            return unauthorized()

        if not has_permission(jwt_payload, user_id):
            return forbidden()

        intents = IntentModel.get_by_chatbot_id(chatbot_id)
        return {"intents": [i.json() for i in intents]}, 200

    @jwt_required()
    def post(self, user_id, chatbot_id):
        jwt_payload = get_jwt_identity()
        if not is_authenticated(jwt_payload, user_id):
            return unauthorized()

        if not has_permission(jwt_payload, user_id):
            return forbidden()

        data = IntentList.parser.parse_args()
        intent = IntentModel(name=data["name"], chatbot_id=chatbot_id)
        intent.save()
        return intent.json(), 201
