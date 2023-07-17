from marshmallow import Schema, fields


class Favorites:
    __table__ = 'favorites'

    def __init__(self, id, id_author, id_offer):
        self.id = id
        self.id_author = id_author
        self.id_offer = id_offer



class FavoritesSchema(Schema):
    id = fields.Int()
    id_author = fields.Str()
    id_offer = fields.Int()