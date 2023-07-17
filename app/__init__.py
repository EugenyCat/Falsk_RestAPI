from flask import Flask, g
from flask_restx import Api
from app.api.database.database import Postgre_SQL
from app.api.views.users import users_ns, user_ns
from app.api.views.joboffers import joboffer_ns, joboffers_ns
from app.api.views.favorites import favorite_ns, favorites_ns

from app.api.dao.user import UserDAO
from app.api.services.user import UserService
from app.api.views.users import UserView

from app.api.dao.joboffer import JobOfferDAO
from app.api.services.joboffer import JobOfferService
#from app.api.views.joboffers import JobOffersView


from app.api.dao.favorite import FavoriteDAO
from app.api.services.favorite import FavoriteService


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.app_context().push()
    return app

def configure_app(app):
    api = Api(app)
    api.add_namespace(users_ns)
    api.add_namespace(user_ns)
    api.add_namespace(joboffer_ns)
    api.add_namespace(joboffers_ns)
    api.add_namespace(favorite_ns)
    api.add_namespace(favorites_ns)


app = create_app()
configure_app(app)


@app.route('/index/')
def index():
    return UserView().get()


@app.before_request
def before_request():
    g.con_psql = Postgre_SQL()
    g.session = g.con_psql.get_connection()

    g.user_dao = UserDAO(g.session)
    g.user_service = UserService(g.user_dao)

    g.joboffer_dao = JobOfferDAO(g.session)
    g.joboffer_service = JobOfferService(g.joboffer_dao)

    g.favorite_dao = FavoriteDAO(g.session)
    g.favorite_service = FavoriteService(g.favorite_dao)
    #g.user = current_user


@app.teardown_request
def teardown_request(error):
    if g.con_psql is not None:
        g.con_psql.close_connection()