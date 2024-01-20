# Get Image GeoTags
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
from datetime import datetime



# Fxn to Get Human Readable Time
def get_readable_time(mytime):
	return datetime.fromtimestamp(mytime).strftime('%Y-%m-%d-%H:%M')


def get_exif(filename):
    exif = Image.open(filename)._getexif()

    if exif is not None:
        for key, value in exif.items():
            name = TAGS.get(key, key)
            exif[name] = exif.pop(key)

        if 'GPSInfo' in exif:
            for key in exif['GPSInfo'].keys():
                name = GPSTAGS.get(key,key)
                exif['GPSInfo'][name] = exif['GPSInfo'].pop(key)

    return exif

def get_coordinates(info):
    for key in ['Latitude', 'Longitude']:
        if 'GPS'+key in info and 'GPS'+key+'Ref' in info:
            e = info['GPS'+key]
            ref = info['GPS'+key+'Ref']
            info[key] = ( str(e[0][0]/e[0][1]) + '°' +
                          str(e[1][0]/e[1][1]) + '′' +
                          str(e[2][0]/e[2][1]) + '″ ' +
                          ref )

    if 'Latitude' in info and 'Longitude' in info:
        return [info['Latitude'], info['Longitude']]

def get_decimal_coordinates(info):
    if info is not None:
        coordinates = {}
        for key in ['Latitude', 'Longitude']:
            gps_key = 'GPS' + key
            gps_key_ref = gps_key + 'Ref'
            
            if gps_key in info and gps_key_ref in info:
                coordinates[key] = str(info[gps_key]) + ' ' + str(info[gps_key_ref])
                
        return coordinates if coordinates else None
    else:
        return None

    if 'Latitude' in info and 'Longitude' in info:
        return [info['Latitude'], info['Longitude']]
