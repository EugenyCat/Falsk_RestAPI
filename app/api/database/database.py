import psycopg2
from app.config import DATABASE_URL


class Postgre_SQL:

    def __init__(self):
        self.connection = psycopg2.connect(DATABASE_URL)

    def get_connection(self):
        return self.connection

    def close_connection(self):
        self.connection.close()

