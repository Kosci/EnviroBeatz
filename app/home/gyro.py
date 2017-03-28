from app.models import Song
from app.home import data

def skip_song():
	gyros = data.getGyroData()
	
	is_shaking = False
	keys = gyros.keys()
	pos_orientation = (gyros[keys[0]] > 0)
	for key in keys():
		for coord in gyros[key]:
			if coord<0 and pos_orientation:
				pos_orientation = False
				is_shaking = True
			elif coord>0 and !pos_orientation:
				pos_orientation = True
				is_shaking = True
	if is_shaking:
		return Song.query().first()