import json
import urllib.request
import urllib.parse
import pairdata
import sys




class Purple_Obj:
    '''
    class which creates a sensor object
    '''

    def __init__(self, AQI: int, lat: float, lon: float):
        self.AQI = AQI
        self.lat = lat
        self.lon = lon

    def get_AQI(self):
        return self.AQI

    def get_Lat(self):
        return self.lat

    def get_Lon(self):
        return self.lon

class ReverseNominatimFile:
    '''
    takes coordinates from json object and returns description of location through file path
    '''
    def __init__(self, path: str):
        response = None

        try:
            response = open(path, mode = 'r')
            data = json.load(response)
            self.location = None
            for i in data:
                if i == 'display_name':
                    self.location = data[i]
                    
        except TypeError:
            print(f'FAILED\n{path}\nFORMAT')
            sys.exit(0)

        except json.JSONDecodeError:
            print(f'FAILED\n{path}\nFORMAT')
            sys.exit(0)

        except FileNotFoundError:
            print(f'FAILED\n{path}\nMISSING')
            sys.exit(0)
        
        finally:
            if response != None:
                response.close()


    def get_location(self):
        return self.location


class ReverseNominatimAPI:
    def __init__(self, lat: float, lon: float):

        try:
            request = urllib.request.Requestprint(request)
            response = urllib.request.urlopen(request).read()
            #print(response)
            data = json.loads(response)
            self.location = ''
            for i in data:
                if i == 'display_name':
                    self.location = data[i]
                    #print(self.location)
                    
        except json.JSONDecodeError:
            print(f'FAILED\nhttps://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}\nFORMAT')
            sys.exit(0)

        except FileNotFoundError:
            print(f'FAILED\nhttps://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}\nMISSING')
            sys.exit(0)

        except TypeError:
            print(f'FAILED\nhttps://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}\nFORMAT')
            sys.exit(0)

    def get_location(self):
        return self.location


def getlocation(purpleobjects: list['purpleairobjects'], location: str):
        final_location = []
        if location.split()[1] == 'FILES':
            for i in location.split()[2:]:
                locat = ReverseNominatimFile(i)
                c = locat.get_location()
                final_location.append(c)

        elif location.split()[1] == "NOMINATIM":
            for i in purpleobjects:
                locat = ReverseNominatimAPI(i.lat(), i.lon())
                c = locat.get_location()
                final_location.append(c)

        return final_location



        
    
