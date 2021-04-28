from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config.db import db
from resources.chatbot import Chatbot

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

api = Api(app)
api.add_resource(Chatbot, "/")

Migrate(app, db)
