import pairdata
import json
import sys


class PurpleObjects:
    '''
    Initializes a constructor sensor object 
    '''
    
    def __init__(self, lat: float, lon: float):
        
        self.lat = lat
        self.lon = lon

    def latitude(self):
        return self.lat
    
    def longitude(self)
        return self.lon



def runPurple(center: tuple, dist: str, thresh: str, num: str, data: str, reverse: str) -> list:
    '''
    starts the work of finding valid places and returns a list of tuples which contains
    data from valid sensors
    '''
    
    if data.split()[:2] == ['AQI', 'PURPLEAIR']:
        p = PurpleAPI()
    elif data.split()[:2] == ['AQI', 'FILE']:
        p = PurpleFile(data.split()[2])

    dist = _to_integer(dist)
    thresh = _to_integer(thresh)
    num = _to_integer(num)

    valid_places = _valid_places(p, center, dist, thresh)
        
    if valid_places == None:
        return None
        
    order_places = _order_places(p, valid_places, num)
        
    descriptions = nominatim_functions.reverse(order_places, reverse)

    return _make_tuples(order_places, descriptions)

#private classes
    
def _valid_places(p: 'Purple', center: tuple, dist: int, thresh: int) -> list:
    '''
    finds every valid place and returns them as a list
    '''
    
    places = []
    for index, locations in enumerate(p.get_data()):
        if aqi_math.find_aqi(p.get_pm(index)) >= thresh and p.get_age(index) <= 3600 and p.get_Type(index) == 0 and aqi_math.find_dist(p.get_Lat(index), center[0], p.get_Lon(index), center[1], dist) <= dist:
            places.append(Purple_Obj(aqi_math.find_aqi(p.get_pm(index)), p.get_Lat(index), p.get_Lon(index)))
    return places

def _order_places(p: 'Purple', valid_places: list, num: int) -> list:
    '''
    orders the places in terms of AQI and returns top N locations
    '''
    
    x = sorted(valid_places, key = lambda x: x.AQI, reverse = True)
    if x == None:
        print("No list")
    elif len(x) > num:
        return x[:num]
    else:
        return x

def _make_tuples(purples: list['purples'], descriptions: str) -> list:
    '''
    turns the list of sensors and location descriptions as formatted list of tuples
    '''
    
    ret_list = []
    for purple, desc in zip(purples, descriptions):
        ret_list.append((purple.get_AQI(), (purple.get_Lat(), purple.get_Lon()), desc))
    return ret_list


def _to_integer(string: str) -> int:
    '''
    converts string to integer
    '''
    
    return int(string.split()[1])
