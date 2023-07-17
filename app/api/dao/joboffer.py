from psycopg2.extras import RealDictCursor
import json


#QUERIES
from app.api.dao.sql.joboffer.get_all import QUERY_GET_ALL_JOBOFFER
from app.api.dao.sql.joboffer.get_one import QUERY_GET_JOBOFFER
from app.api.dao.sql.joboffer.post import QUERY_POST_JOBOFFER
from app.api.dao.sql.joboffer.put import QUERY_PUT_JOBOFFER
from app.api.dao.sql.joboffer.delete import QUERY_DELETE_JOBOFFER


#CRUD
class JobOfferDAO:
    def __init__(self, connection):
        self.connection = connection


    # Get
    def get_all(self):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_GET_ALL_JOBOFFER, ())
                return json.loads(json.dumps(cursor.fetchall()))


    # Get
    def get_one(self, id:int):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_GET_JOBOFFER, (id, ))
                return json.loads(json.dumps(cursor.fetchone()))


    # Post (create one new joboffer)
    def post(self, data):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_POST_JOBOFFER, (*data, ))
                return self.get_one(data['id'])

    # Put (update every field
    def put(self, data):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(QUERY_PUT_JOBOFFER, (*data,))
            return self.get_one(data['id'])


    # Patch (update particular)
    def patch(self, data):
        pass


    # Delete
    def delete(self, id:int):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(QUERY_DELETE_JOBOFFER, (id,))
            return ""