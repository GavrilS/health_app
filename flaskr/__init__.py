from flask import (
    Flask
)
from flaskr.routes.article import article
from flaskr.routes.base import home


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)
    app.register_blueprint(article)

    return app