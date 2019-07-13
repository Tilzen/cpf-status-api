from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .serializer import configure_marshmallow
from .models.tables import configure_database


def create_app():
    """
    application factory.
    """

    app = Flask(__name__)
    app.config.from_object('config')

    configure_database(app)
    configure_marshmallow(app)

    Migrate(app, app.db)
    JWTManager(app)

    from .api import bp_api
    app.register_blueprint(bp_api)

    from .user import bp_user
    app.register_blueprint(bp_user)

    from .login import bp_login
    app.register_blueprint(bp_login)

    return app
