# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

app = Flask(__name__)
db = SQLAlchemy(app)
clientid = 'b7966d22e02437e5d5dcce50cd95ce8d'

def create_app():
    from app import models

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .home import cloud

    db.create_all()
    db.session.commit()

    return app
