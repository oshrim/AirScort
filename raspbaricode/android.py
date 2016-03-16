import requests
import json
from Vehicle import Vehicle


class Android():
    
    
    def __init__(self):

        self.url = 'http://airscort-server1.meteor.com/api/drone/location/drone/1/station/1/event/1/location/11.11111111/22.2222222/3.3/battery/51'

        
    def getLatAndLon(self):
     
        r= requests.post(self.url)
                    
        data =r.json()
        lat = float(data['lat'])
        lon = float(data['lon'])
        
        #print 'lat: %s' %lat
        #print  'lon: %s' %lon
     	
        return [lat,lon]
    


