from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp

from models.user import UserModel

BLANK_ERROR = "'{}' cannot be left blank"
INVALID_CREDENTIALS = "Invalid credentials"
USER_ALREADY_EXISTS = "A user with name '{}' already exists"
USER_CREATED = "User created successfully"

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username", type=str, required=True, help=BLANK_ERROR.format("username")
)
_user_parser.add_argument(
    "password", type=str, required=True, help=BLANK_ERROR.format("password")
)


class UserRegister(Resource):
    @classmethod
    def post(cls):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": USER_ALREADY_EXISTS.format(data["username"])}

        user = UserModel(**data)
        user.save_to_db()

        return {"message": USER_CREATED}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = _user_parser.parse_args()

        user = UserModel.find_by_username(data["username"])

        if user and safe_str_cmp(user.password, data["password"]):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
            }, 200

        return {"message": INVALID_CREDENTIALS}, 401
