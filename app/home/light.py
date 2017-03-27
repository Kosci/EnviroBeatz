from app.models import SongLight, Song
from app.home import data

def getNextSong():
    avgEnv = data.averageEnvironmentData()
    songLight = SongLight.query.filter(
        SongLight.light_max > avgEnv.light and SongLight.light_min < avgEnv.light
    ).first()

    song = Song.query.filter_by(id=SongLight.song_id)
    return song