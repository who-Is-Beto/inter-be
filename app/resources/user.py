from uuid import uuid4
from flask_smorest import Blueprint, abort 
from flask.views import MethodView
from app.scheemas import UserSchema
from app.db import users

blueprint = Blueprint("user", "users", description="User operations")

@blueprint.route("/users/<string:user_id>")
class User(MethodView):
    @blueprint.response(200, UserSchema)
    def get(_, user_id):
        user = users.get(user_id)
        if not user :
            abort(404, "User not found")
        return user

@blueprint.route("/users")
class UserList(MethodView):
    @blueprint.arguments(UserSchema)
    @blueprint.response(201, UserSchema)
    def post(self, user):
        user_id = uuid4().hex
        new_user = {"id": user_id, **user}
        # TODO: ADD A DATABASE WITH ORM HERE
        users[user_id] = new_user
        return new_user