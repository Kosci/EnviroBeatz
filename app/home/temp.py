from flask import jsonify
from app.models import SongTemperature, Song
from app.home import data

def getNextSong():
    avgEnv = data.averageEnvironmentData()
    songTemp = SongTemperature.query.filter(SongTemperature.temp_min < avgEnv.room_temp).filter(SongTemperature.temp_max > avgEnv.room_temp).first()
    song = jsonify(Song.query.filter_by(id=songTemp.song_id).first().url)
    return song