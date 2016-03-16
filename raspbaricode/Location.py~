

class Location:


	#######################################
	# Constructor
	#######################################
	def __init__(self, _latitude=0.0, _longitude=0.0, _altitude=0.0):
		self.latitude  = _latitude
		self.longitude = _longitude
		self.altitude  = _altitude
   
   
	#######################################
	# Getters
	#######################################
	def get_latitude(self):
		return self.latitude;
	
	def get_longitude(self):
		return self.longitude;
		
	def get_altitude(self):
		return self.altitude;

	#######################################
	# Setters
	#######################################
	def set_latitude(self, _latitude):
		self.latitude = _latitude;
	
	def set_longitude(self, _longitude):
		self.longitude = _longitude;
		
	def set_altitude(self, _altitude):
		self.altitude = _altitude;

	
	#######################################
	# Equals
	#######################################	
	def equalsTo(self, cmpLocation):	
		if cmpLocation.latitude == self.latitude and cmpLocation.longitude == self.longitude and cmpLocation.altitude == self.altitude:
			return True
		else:
			return False
		
	
	#######################################
	# Convert From Vehicle Location
	#######################################	
	def setFromVehicleLocation(self, vecLoc):
		self.latitude  = vecLoc.lat
		self.longitude = vecLoc.lon
		self.altitude  = vecLoc.alt
		
	#######################################
	# Convert From JSON Location
	#######################################	
	def setFromJSONLocation(self, JSONLoc):
		self.latitude  = JSONLoc['latitude']
		self.longitude = JSONLoc['longitude']
		self.altitude  = JSONLoc['altitude']
		
		
		
	#######################################
	# Print Location
	#######################################
	def displayLocation(self):
		print "|  latitude: %f  |  longitude: %f  |  altitude: %f  " % (self.latitude, self.longitude, self.altitude)
		
