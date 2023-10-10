from apps.database import init_db
from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Database
    with app.app_context():
        init_db()

    return app
