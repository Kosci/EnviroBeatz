from flask import jsonify, abort, make_response

from . import home

# Working with mock data until service can use real data from db
songs = [
    {
        'id' : u'301361791',
        'title' : u'Deep In The Night (Muzzy Remix)',
        'artist' : u'Pegboard Nerds, Snails, Muzzy'
    },
    {
        'id' : u'229562445',
        'title' : u"It's Me",
        'artist' : u'Spag Heddy'
    }
]

baseURL = '/envirobeatz/api/v1.0/'

@home.route(baseURL + 'songs', methods=['GET'])
def get_songs():
    return jsonify({'songs' : songs})

@home.route(baseURL + 'songs/<string:song_id>', methods=['GET'])
def get_song(song_id):
    song = [song for song in songs if song['id'] == song_id]
    if len(song) == 0:
        abort(404)
    return jsonify({'songs' : song[0]})

@home.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error' : 'Not found'}), 404)
