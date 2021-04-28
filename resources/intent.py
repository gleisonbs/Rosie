from flask_restful import Resource, reqparse

from models.intent_model import IntentModel


class IntentList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name", type=str, required=True, help="This field is mandatory"
    )

    def get(self, chatbot_id):
        intents = IntentModel.get_by_chatbot_id(chatbot_id)
        return {"intents": [i.json() for i in intents]}, 200

    def post(self, chatbot_id):
        data = IntentList.parser.parse_args()
        intent = IntentModel(name=data["name"], chatbot_id=chatbot_id)
        intent.save()
        return intent.json(), 201
