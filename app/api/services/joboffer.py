from flask import request
from app.api.dao.joboffer import JobOfferDAO


class JobOfferService:
    def __init__(self, joboffer_dao: JobOfferDAO):
        self.joboffer_dao = joboffer_dao


    def get_all(self) -> list['joboffer']:
        return self.joboffer_dao.get_all()


    def get_one(self, id:int):
        return self.joboffer_dao.get_one(id)


    def post(self):
        req_data = request.json
        return self.joboffer_dao.post(**req_data)


    def put(self, author:int):
        req_data = request.json
        req_data['author'] = author
        return self.joboffer_dao.put(**req_data)


    def patch(self):
        pass


    def delete(self, id:int):
        return self.joboffer_dao.delete(id)