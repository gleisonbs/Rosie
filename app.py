from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from config.db import db
from resources.chatbot import Chatbot, ChatbotList
from resources.intent import IntentList
from resources.user import UserLogin, UserRegister

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = "b59dc17d-e6f8-4ad4-8eff-7d1594dd030d"

JWTManager(app)

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api = Api(app)
api.add_resource(ChatbotList, "/chatbot")
api.add_resource(Chatbot, "/chatbot/<string:name>")

api.add_resource(IntentList, "/chatbot/<int:chatbot_id>/intent")

api.add_resource(UserRegister, "/signup")
api.add_resource(UserLogin, "/signin")

Migrate(app, db)
