import json
import urllib.request
import urllib.parse
import pairdata
import sys

class ForwardNominatimFile:
    '''
    responsible for creating a forward geocoding object and returning the coordinates
    '''

    def __init__(self, path: str):

        response = None
        
        try:
            response = open(path, mode='r')
            data = json.load(response)
            self.lat = None
            self.lon = None
            for i in data[0]:
                if i == 'lat':
                    self.lat = float(data[0][i])
                if i == 'lon':
                    self.lon = float(data[0][i])
                    
        except json.JSONDecodeError:
            print(f'FAILED\n{path}\nFORMAT')
            sys.exit(0)

        except FileNotFoundError:
            print(f'FAILED\n{path}\nMISSING')
            sys.exit(0)

        except TypeError:
            print(f'FAILED\n{path}\nFORMAT')
            sys.exit(0)

        finally:
            if response != None:
                response.close()

    def latitude_longitude(self):
        '''
        parses through file to find latitude and longitude
        '''
        return self.lat, self.lon

    


class ForwardNominatimAPI:
    '''
    connects to Nominatim API and returns the coordinates
    '''
    def __init__(self, place: str):

        try:
        
            place = urllib.parse.urlencode([('q', place)])
            #print(place)
            request = urllib.request.Request(f'https://nominatim.openstreetmap.org/search?{place}&format=json')
            #print(request)
            response = urllib.request.urlopen(request).read()
            #print(response)
            data = json.loads(response)
            self.lat = None
            self.lon = None
            for i in data[0]:
                if i == 'lat':
                    self.lat = float(data[0][i])
                if i == 'lon':
                    self.lon = float(data[0][i])
                    
        except json.JSONDecodeError:
            print(f'FAILED\n{place}\nFORMAT')
            sys.exit(0)

        except FileNotFoundError:
            print(f'FAILED\n{place}\nMISSING')
            sys.exit(0)

        except TypeError:
            print(f'FAILED\n{place}\nFORMAT')
            sys.exit(0)


    def latitude_longitude(self):
        '''
        gets latitude and longitude
        '''
        return self.lat, self.lon
    
    
def get_coordinates(location: str):
    '''
    uses forward geocoding to get the coordinates given a location
    '''
    if location.split()[1] == 'NOMINATIM':
        coordinates = ForwardNominatimAPI(location[17:])
    elif location.split()[1] == 'FILES':
        coordinates = ForwardNominatimAPI(location[12:])
        
    return coordinates.latitude_longitude()          
    



        
        
