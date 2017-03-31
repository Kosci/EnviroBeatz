from flask import jsonify, abort, make_response
from flask import jsonify, abort, make_response, request, redirect
from app.models import Song
from app import db
from flask_sqlalchemy import SQLAlchemy
from . import home

# Working with mock data until service can use real data from db
songs = [
    {
        'url' : u'https://soundcloud.com/disciple/calamari',
        'title' : u'Calamari',
        'artist' : u'Dubloadz, Barely Alive'
    },
    {
        'url' : u'https://soundcloud.com/contrvbvnd/contrvbvnd-m2-original-mix-1',
        'title' : u"M2",
        'artist' : u'Contrvbvnd'
    }
]

baseURL = '/envirobeatz/api/v1.0/'

@home.route(baseURL + 'songs', methods=['GET'])
def get_songs():
    urls = list()

    for song in songs:
        urls.append(song['url'])

    return jsonify({'songs' : urls})

@home.route(baseURL + 'songs/<string:song_id>', methods=['GET'])
def get_song(song_id):
    song = [song for song in songs if song['id'] == song_id]
    if len(song) == 0:
        abort(404)
    return jsonify({'songs' : song[0]})

@home.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error' : 'Not found'}), 404)

@home.route(baseURL + 'songs/add', methods=['POST'])
def add_song():
    song = Song(url=request.form['songUrl'], song_title=request.form['songTitle'], mood_id=request.form['moodId'])
    db.session.add(song)
    db.session.commit()
    return make_response(redirect('/'))
