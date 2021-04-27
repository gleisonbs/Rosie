from api.ma import ma
from api.models.chatbot_model import Chatbot


class ChatbotSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Chatbot
        load_instance = True
