from flask import request
from app.api.dao.favorite import FavoriteDAO


class FavoriteService:
    def __init__(self, favorite_dao: FavoriteDAO):
        self.favorite_dao = favorite_dao


    def get_all(self) -> list['favorite']:
        return self.favorite_dao.get_all()


    def get_one(self, id:int):
        return self.favorite_dao.get_one(id)


    def post(self):
        req_data = request.json
        return self.favorite_dao.post(**req_data)


    def put(self):
        req_data = request.json
        return self.favorite_dao.put(**req_data)


    def patch(self):
        pass


    def delete(self, id:int):
        return self.favorite_dao.delete(id)