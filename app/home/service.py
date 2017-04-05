from flask import jsonify, abort, make_response
from flask import jsonify, abort, make_response, request, redirect
from app.models import Song
from app import db
from flask_sqlalchemy import SQLAlchemy
from . import home
from app.home import combineData

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
    songUrl = request.form['songUrl']
    songType = request.form['songType']
    eMin = request.form['min']
    eMax = request.form['max']

    song = Song(url=songUrl)
    db.session.add(song)
    db.session.flush()

    if songType.lower() == 'temperature':
        envSong = SongTemperature(song_id=song.id, temp_min=eMin, temp_max=eMax)
    else:
        envSong = SongLight(song_id=song.id, light_min=eMin, light_max=eMax)

    db.session.add(envSong)
    db.session.commit()
    return make_response(redirect('/'))

@home.route(baseURL + 'songs/random', methods=['GET'])
def get_random():
    return combineData.combine()['url']
