from app.home import temp, light
import random

def combine():

    songs = list()
    songs.append(light.getNextSong())
    songs.append(temp.getNextSong())

    return random.choice(songs)