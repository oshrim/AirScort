from Vehicle import Vehicle
from Location import Location
import followme
import time
import json
import requests


##############################################
#				Consts						 #
##############################################
DRONE_ID      	= 1		# Drone individual id
INTERVAL_TIME 	= 0.5	# Time between each loop (sec)
TAKE_OFF_ALT  	= 2		# Take Off altitude (meters)
GOTO_ALT		= 3		# Go-To altitude (meters)
GOTO_SPEED		= 1		# Go-To speed (meters/sec)
CONNECT_TIMEOUT	= 1.0	# Timeout for the connection (sec)
READ_TIMEOUT	= 5.0	# Timeout for the connection (sec)
FAIL		  	= -1	# Fail


##############################################
#				Main Program				 #
##############################################
def main():
	
	


	#followme
    followme.main()




"""


	##############################################
	#			Pre Loop Script					 #
	##############################################
	
	print "Starting Script \n===============\n"
	vec = Vehicle('/dev/ttyAMA0')			# UART connection
	vec.arm_and_takeoff(TAKE_OFF_ALT)		# Meters

	# initial locations
	drone_id			= DRONE_ID
	target  	  		= Location(0.0, 0.0, 0.0)
	last_target  	  	= Location(0.0, 0.0, 0.0)
	drone_location 		= Location(0.0, 0.0, 0.0)
	
	#initial mission id
	mission_id = -1		# Represent the drone mission
	
	#vehicle_condition_yaw(heading, relative=False)		# Set the face direction of the drone
	
	
	
	##############################################
	#				Main Loop					 #
	##############################################
	while True:
		break
		if vec.get_mode() != "GUIDED" and vec.get_mode() != "RTL":
			print "Flight mode is not GUIDED or RTL"
			break
		
		
		# Drone current parameters #
		# ======================== #
		drone_battery	= vec.get_battery_level()					# Get drone battery level
		drone_location.setFromVehicleLocation(vec.get_location())	# Get drone current location
		check_drone_info(drone_location, drone_battery)				# Check if the drone info is valid
		print "Location ==> | lat: $%f  |  lng: $%f  |  alt: $%f  |  battery: $%f  |" % (drone_location.latitude, drone_location.longitude, drone_location.altitude, drone_battery)
		
		# Get drone target from server
		targetJSON = send_location_to_server(mission_id, drone_id, drone_location.latitude, drone_location.longitude, drone_location.altitude, drone_battery)
		
		if not (targetJSON == FAIL):
			# Set drone target
			target.setFromJSONLocation(targetJSON)
			
			
			# Execute sserver command
			if targetJSON is not None:
				try: 
					#print target['mission_id']
					if targetJSON['mission_id'] != mission_id:
						mission_id = targetJSON['mission_id']
						print "New mission id: $%f " % (targetJSON['mission_id'])
				except KeyError: 
					print "mission_id not exist - RTL"
					#vec.vehicle_RTL()
					
				
				# Check server command for new target
				if not (target.equalsTo(last_target)):
					print "===-> Going to new destination: | lat: $%f  |  lng: $%f  |  alt: $%f  |" % (target.latitude,  target.longitude, target.altitude )
					vec.simpleGoTo(target.latitude, target.longitude, GOTO_ALT, GOTO_SPEED)
					vec.print_vehicle_full_state_info()
					last_target = target

			print "\n"
			#vec.print_vehicle_state()
		else:
			print "MAIN =====> JSON FAIL\n\n"
			
		
	vec.closeVec()

	
	
##############################################
#			Send Location To Server			 #
##############################################
# Sent the current drone location to server and return the server command
def send_location_to_server(mission_id, drone_id, drone_location_lat, drone_location_lng, drone_location_alt, drone_battery):
	request_string  = "http://agri-airscort.meteor.com/api/agri/drone/location/drone/%s/mission/%s/location/%f/%f/%f/battery/%s" %(drone_id, mission_id, drone_location_lat, drone_location_lng, drone_location_alt, drone_battery)

	# Server connection
	try:
		req = requests.post(request_string + "",  json={"key": "value"} ,timeout=(CONNECT_TIMEOUT, READ_TIMEOUT))
		time.sleep(INTERVAL_TIME)
		#print(req.status_code)
		#print(req.json())
	
	except requests.exceptions.RequestException:
		print "** Connection Error - RequestException"
		return FAIL
		
	except requests.exceptions.ConnectTimeout as e:
		print "** Connection Error - ConnectTimeout"
		return FAIL
		
		
		
	if(req):
		try:
			server_response = json.loads(req.text) #Convert server response to json
			print "Target   ==> | lat: $%f  |  lng: $%f  |  alt: $%f  |" % (server_response['latitude'], server_response['longitude'], server_response['altitude'])
		except ValueError, e:
			print "Fail to convert server response to json"
			return FAIL
		return server_response
	else:
		return FAIL
	
	
##############################################
#			Check Drone Info				 #
##############################################
def check_drone_info(drone_location, drone_battery):
	print "=================== ERRORS ============================="
	if not (drone_location.latitude):
		print "ERROR lat"
		drone_location.set_latitude(0.0)
	
	if not (drone_location.longitude):
		print "ERROR lon"
		drone_location.set_longitude(0.0)
		
	if not (drone_location.altitude):
		print "ERROR alt"
		
	if not (drone_battery):
		print "ERROR bat"
	
	print "======================================================"



##############################################
#				Main Loop					 #
##############################################

"""
if __name__ == "__main__":

    main()


	
