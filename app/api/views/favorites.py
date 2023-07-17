from flask_restx import Resource, Namespace
from app.api.dao.model.favorite import FavoritesSchema
from flask import  g


favorites_ns = Namespace('favorites')
favorite_ns = Namespace('favorite')

favorites_schema = FavoritesSchema(many=True)
favorite_schema = FavoritesSchema()


@favorites_ns.route('')
class FavoriteView(Resource):
    # Get all users
    def get(self):
        all_favorites = g.favorite_service.get_all()
        return favorites_schema.dump(all_favorites), 200


    # Create/Add one new user
    def post(self):
        return g.favorite_service.post(), 200


@favorite_ns.route('')
class JobOfferView(Resource):
    # Get one
    def get(self, fid):
        favorite = g.favorite_service.get_one(fid)
        return favorite_schema.dump(favorite), 200


    # Put (update every field)
    def put(self, fid):
        favorite = g.favorite_service.put(fid)
        return favorite_schema.dump(favorite), 200


    # Patch (update particular)
    def patch(self, oid):
        pass


    # Delete
    def delete(self, fid):
        g.favorite_service.delete(fid)
        return "", 200