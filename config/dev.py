from flask_jwt_extended import JWTManager

from config.db import db


def config_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "b59dc17d-e6f8-4ad4-8eff-7d1594dd030d"

    JWTManager(app)

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()
