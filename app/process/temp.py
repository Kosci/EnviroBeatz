from app.models import SongTemperature
from app.process import data

def getNextSong():
    data.averageEnvironmentData()
    return