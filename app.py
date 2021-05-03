from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    from config.dev import config_db
    from config.routes import config_routes

    config_db(app)
    config_routes(app)

    app.run("0.0.0.0", 5000)
