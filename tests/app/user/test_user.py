import json
from unittest import TestCase

from app import app
from config.db import db
from config.dev import config_db
from config.routes import config_routes


class TestUser(TestCase):
    @classmethod
    def setUpClass(self):
        config_db(app)
        config_routes(app)

    def setUp(self):
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_can_create_user_successfully(self):
        with app.test_client() as c:
            response = c.post(
                "/signup",
                data=json.dumps({"username": "test.user", "password": "1234"}),
                content_type="application/json",
            )
            self.assertEqual(response.status_code, 201)

    def test_cannot_create_user_that_already_exists(self):
        with app.test_client() as c:
            c.post(
                "/signup",
                data=json.dumps({"username": "test.user", "password": "1234"}),
                content_type="application/json",
            )
            response = c.post(
                "/signup",
                data=json.dumps({"username": "test.user", "password": "1234"}),
                content_type="application/json",
            )
            self.assertEqual(response.status_code, 409)
