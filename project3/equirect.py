import math

def equirectangular(lat1: float, lat2: float, lon1: float, lon2: float) -> float:
    '''
    calculates the distance between two points on Earth and returns it
    '''
    
    R = 3958.8
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    alat = (lat2 + lat1) / 2
    x = dlon * math.cos(alat)
    d = math.sqrt((x*x) + (dlat * dlat)) * R

    return d
