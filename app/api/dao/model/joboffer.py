from marshmallow import Schema, fields


class JobOffer:
    __table__ = 'joboffer'

    def __init__(self, id, author, title, offer_description, still_list):
        self.id = id
        self.author = author
        self.title = title
        self.offer_description = offer_description
        self.still_list = still_list


class JobOfferSchema(Schema):
    id = fields.Int()
    author = fields.Str()
    title = fields.Str()
    offer_description = fields.Str()
    still_list = fields.Str()