from marshmallow import Schema, fields

class User:
    __tablename__ = 'users'

    def __init__(self, id, name, email, password, account_type,
                 second_name=None,
                 country=None,
                 city=None,
                 phone_number=None,
                 gender=None,
                 avatar=None,
                 role=False):

        self.id = id
        self.name = name
        self.email = email
        self.second_name = second_name
        self.country = country
        self.city = city
        self.phone_number = phone_number
        self.gender = gender
        self.password = password
        self.account_type = account_type
        self.avatar = avatar
        self.role = role



class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()
    second_name = fields.Str()
    country = fields.Str()
    city = fields.Str()
    phone_number = fields.Str()
    gender = fields.Str()
    password = fields.Str()
    account_type = fields.Str()
    avatar = fields.Str()
    role = fields.Str()