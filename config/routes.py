from flask_restful import Api

from resources.chatbot import Chatbot, ChatbotList
from resources.intent import Intent, IntentList
from resources.user import UserLogin, UserRegister


def config_routes(app):
    api = Api(app)
    api.add_resource(ChatbotList, "/user/<int:user_id>/chatbot")
    api.add_resource(Chatbot, "/user/<int:user_id>/chatbot/<string:name>")

    api.add_resource(
        IntentList, "/user/<int:user_id>/chatbot/<int:chatbot_id>/intent"
    )
    api.add_resource(
        Intent,
        "/user/<int:user_id>/chatbot/<int:chatbot_id>/intent/<string:name>",
    )

    api.add_resource(UserRegister, "/signup")
    api.add_resource(UserLogin, "/signin")
