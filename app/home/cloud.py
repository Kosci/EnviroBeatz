import json
from app.models import *
from urllib2 import urlopen


# get the last 5 cached sets of values
# return a list of the 5 sets
def get_data():
    response = urlopen('https://dweet.io/get/dweets/for/envirobeatz').read()

    # convert HTTP bytes to string with decode('utf8')
    # set as dictionary
    data_dictionary = json.loads(response.decode('utf8'))
    if data_dictionary['with'] == 404:
        return []

    # store the 5 latest cached sets of data in a list
    cached_data = list()
    for i in range(0, 5):
        cached_data.append(data_dictionary['with'][i]['content'])

    return cached_data

# store the 5 recent cached sets of data
def store_data():
    data = list()
    data = get_data()

    for each in data:
        environment = Environment(gyro_x = each['gyro_x'],
                                  gyro_y = each['gyro_y'],
                                  gyro_z = each['gyro_x'],
                                  sensor_temp = each['object_temp'],
                                  room_temp = each['ambient_temp'],
                                  compass_x = each['compass_x'],
                                  compass_y = each['compass_y'],
                                  compass_z = each['compass_z'],
                                  accel_x = each['acc_x'],
                                  accel_y = each['acc_y'],
                                  accel_z = each['acc_z'],
                                  air_pressure = each['air_pressure'],
                                  light = each['light']
                              )

        db.session.add(environment)
        db.session.commit()