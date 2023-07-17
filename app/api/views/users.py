from flask_restx import Resource, Namespace
from app.api.dao.model.user import UserSchema
from flask import  g


users_ns = Namespace('users')
user_ns = Namespace('user')

users_schema = UserSchema(many=True)
user_schema = UserSchema()




@users_ns.route('/')
class UsersView(Resource):

    # Get all users
    def get(self):
        all_users = g.user_service.get_all()
        return users_schema.dump(all_users), 200

    # Create/Add one new user
    def post(self):
        return g.user_service.post(), 200



@user_ns.route('/<string:email>')
class UserView(Resource):

    # Get one
    def get(self, email: str):
        user = g.user_service.get_one(email)
        return user_schema.dump(user), 200


    # Put (update every field)
    def put(self, email: str):
        user = g.user_service.put(email)
        return user_schema.dump(user), 200


    # Patch (update particular)
    def patch(self, email: str):
        pass


    # Delete
    def delete(self, email:str):
        g.user_service.delete(email)
        return "", 200