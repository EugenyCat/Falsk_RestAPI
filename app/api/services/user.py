from flask import request
from app.api.dao.user import UserDAO

class UserService:

    def __init__(self, user_dao:UserDAO):
        self.user_dao = user_dao


    def get_all(self) -> list['User']:
        return self.user_dao.get_all()


    def get_one(self, email:str):
        return self.user_dao.get_one(email)


    def post(self):
        req_json = request.json
        return self.user_dao.post(**req_json)


    def put(self, email:str):
        req_json = request.json
        req_json['email'] = email
        return self.user_dao.put(**req_json)


    def patch(self, email:str):
        pass


    def delete(self, email:str):
        return self.user_dao.delete(email)

