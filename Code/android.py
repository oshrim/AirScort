import requests
import json

class Android():
    
    
    def __init__(self):
        self.url = 'http://airscort-server1.meteor.com/api/drone/location/drone/1/station/1/event/1/location/11.11111111/22.2222222/3.3/battery/51'
       
        
        
    def getLatAndLon(self):
        print self.url
        r = requests.post(self.url)
        data =r.json()
        lat = float(data['lat'])
        lon = float(data['lon'])
        return [lat,lon]
    