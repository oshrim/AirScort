import requests
import json
from Vehicle import Vehicle


class Android():
    
    
    
    def __init__(self):
        # url for server          
        self.url = 'http://agri-server.cloudapp.net/api/drone/location/drone/1/station/1/event/1/location/11.11111111/22.2222222/3.3/battery/51'          
       
        
    def getLatAndLon(self):
     
        #get data from server
        r= requests.post(self.url,stream=True)
        data =r.json()
        lat = float(data['lat']) # get GPS
        lon = float(data['lon'])
        return [lat,lon]
    

