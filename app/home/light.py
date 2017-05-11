from flask import jsonify
from app.models import SongLight, Song
from app.home import data, cloud

def getNextSong():
    cloud.store_data();
    avgEnv = data.averageEnvironmentData()
    print(avgEnv.light)
    songLight = SongLight.query.filter(SongLight.light_max > avgEnv.light).filter(SongLight.light_min < avgEnv.light).first()

    song = jsonify(Song.query.filter_by(id=songLight.song_id).first().url)
    return song