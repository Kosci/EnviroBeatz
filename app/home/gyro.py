from app.models import Song
from app.home import data

def skip_song():
	gyros = data.getGyroData()
	keys = gyros.keys()
	for key in keys:
		pos_orientation = (gyros[keys[0]] > 0)
		for coord in gyros[key]:
			if coord<0 and pos_orientation:
				pos_orientation = False
				return Song.query().first()
			elif coord>0 and !pos_orientation:
				pos_orientation = True
				return Song.query().first()

		