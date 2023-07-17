from psycopg2.extras import RealDictCursor
import json


#QUERIES
from app.api.dao.sql.favorites.get_all import QUERY_GET_ALL_FAVORITES
from app.api.dao.sql.favorites.get_one import QUERY_GET_ONE_FAVORITES
from app.api.dao.sql.favorites.post import QUERY_POST_FAVORITES
from app.api.dao.sql.favorites.put import QUERY_PUT_FAVORITES
from app.api.dao.sql.favorites.delete import QUERY_DELETE_FAVORITES


#CRUD
class FavoriteDAO:
    def __init__(self, connection):
        self.connection = connection


    # Get
    def get_all(self):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_GET_ALL_FAVORITES, ())
                return json.loads(json.dumps(cursor.fetchall()))


    # Get
    def get_one(self, id:int):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_GET_ONE_FAVORITES, (id, ))
                return json.loads(json.dumps(cursor.fetchone()))


    # Post (create one new joboffer)
    def post(self, data):
        with self.connection:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(QUERY_POST_FAVORITES, (*data, ))
                return self.get_one(data['id'])

    # Put (update every field
    def put(self, data):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(QUERY_PUT_FAVORITES, (*data,))
            return self.get_one(data['id'])


    # Patch (update particular)
    def patch(self, data):
        pass


    # Delete
    def delete(self, id:int):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(QUERY_DELETE_FAVORITES, (id,))
            return ""