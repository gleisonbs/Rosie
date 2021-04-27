from config.ma import ma
from models.chatbot_model import Chatbot


class ChatbotSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Chatbot
        load_instance = True
