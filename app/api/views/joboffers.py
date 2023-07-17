from flask_restx import Resource, Namespace
from app.api.dao.model.joboffer import JobOfferSchema
from flask import  g


joboffers_ns = Namespace('joboffers')
joboffer_ns = Namespace('joboffer')

joboffers_schema = JobOfferSchema(many=True)
joboffer_schema = JobOfferSchema()


@joboffers_ns.route('')
class JobOffersView(Resource):
    # Get all users
    def get(self):
        all_joboffers = g.joboffer_service.get_all()
        return joboffers_schema.dump(all_joboffers), 200


    # Create/Add one new user
    def post(self):
        return g.joboffer_service.post(), 200


@joboffer_ns.route('')
class JobOfferView(Resource):
    # Get one
    def get(self, oid):
        joboffer = g.joboffer_service.get_one(oid)
        return joboffer_schema.dump(joboffer), 200


    # Put (update every field)
    def put(self, oid):
        joboffer = g.joboffer_service.put(oid)
        return joboffer_schema.dump(joboffer), 200


    # Patch (update particular)
    def patch(self, oid):
        pass


    # Delete
    def delete(self, oid):
        g.joboffer_service.delete(oid)
        return "", 200