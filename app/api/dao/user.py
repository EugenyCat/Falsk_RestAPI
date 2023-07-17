from psycopg2.extras import RealDictCursor
import json
from app.api.dao.utils.utils import DateTimeEncoder

#QUERIES
from app.api.dao.sql.user.get_all import QUERY_GET_USERS
from app.api.dao.sql.user.get_one import QUERY_GET_USER_BY_EMAIL
from app.api.dao.sql.user.post import QUERY_POST_USER
from app.api.dao.sql.user.put import QUERY_PUT_USER
from app.api.dao.sql.user.delete import QUERY_DELETE_USER


#CRUD
class UserDAO:
    def __init__(self, connection):
        self.connection = connection

    #Get
    def get_all(self):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_GET_USERS, ())
                return json.loads(json.dumps(cursor.fetchall(), cls=DateTimeEncoder))


    # Get
    def get_one(self, email:str):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_GET_USER_BY_EMAIL, (email, ))
                return json.loads(json.dumps(cursor.fetchone(), cls=DateTimeEncoder))


    # Post (create one new user)
    def post(self, data):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_POST_USER, (*data,))


    # Put (update every field)
    def put(self, data):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_PUT_USER,
                               (*data,))
                return self.get_one(data['email'])


    # Patch (update particular)
    def patch(self, data):
        pass


    # Delete
    def delete(self, email:str):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_DELETE_USER,
                               (email,))