from flask import Flask

import config
from app.models.models import db
from app.routes.routes import users


def create_app():
    app = Flask(__name__)
    app.register_blueprint(users)
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_CONNECTION_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app

app = create_app()