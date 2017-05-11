# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
clientid = 'b7966d22e02437e5d5dcce50cd95ce8d'
clientsecret = '00b4211c800b2b96d2329ead74def040'

def create_app():
    from app import models

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .home import cloud

    db.create_all()
    db.session.commit()

    from app.models import Song, SongLight, SongTemperature

    from sqlalchemy.sql import table, column, select, update, insert
    i = insert(Song)
    i = i.values({"url": "https://soundcloud.com/jd4d/kizzik-mind-blown"})
    db.session.execute(i)
    db.session.commit()
    print(Song.query.first());

    return app
