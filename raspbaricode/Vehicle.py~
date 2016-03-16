from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil # Needed for command message definitions
import socket
import time
import sys
import math


class Vehicle():
   
	#######################################
	# Constructor
	#######################################
	def __init__(self , connectionString):
		print 'Connecting to vehicle on: %s' % connectionString
		self.vehicle = connect(connectionString, baud=57600)
	
	
	#######################################
	# Arm And TakeOff
	#######################################
	def arm_and_takeoff(self,takeOffAltitude):

		#self.vehicle_pre_arm_check()       # chack if the vehicle is armable
		#print "Basic pre-arm checks"
		# Don't let the user try to arm until autopilot is ready
		#while not self.vehicle.is_armable:
		#	print " Waiting for vehicle to initialise..."
		time.sleep(1)

		self.vehicle_arm()						# Arm vehicle
		
		#self.vehicle_arming_check()				# Wait for the drone to arm
		
		time.sleep(1)							# Sleep for Sec
		
		#self.vehicle_take_off(takeOffAltitude)	# TakeOff
		
		self.print_vehicle_full_state_info()	# Print the vehicle status
		

		
#######################################################################################################################################################################
#######################################################################################################################################################################		
#######################################################################################################################################################################		
		
		
		
	##############################################
	#				SETTERS						 #
	##############################################
	
	def air_speed(self,speed):
		self.vehicle.airspeed = speed
		
	def rtl(self):
		self.vehicle.mode = VehicleMode("RTL")
	
	def closeVec(self):
		self.vehicle.close()
	
	def set_mode(self,mode):
		vehicle.mode=mode
	
	def set_armed(self,bool):
		vehicle.armed =bool
			
	def set_groundspeed(self,speed):
		vehicle.groundspeed= speed
		return
	
	
	##############################################
	#				GETTERS						 #
	##############################################

	def get_location(self):                 return self.vehicle.location.global_frame

	def get_location_latitude(self):        return self.vehicle.location.lat

	def get_location_longitude(self):   	return self.vehicle.location.lon

	def get_location_altitude(self):    	return self.vehicle.location.alt
		
	def get_location_global_frame(self):	return self.vehicle.location.global_frame

	def get_location_global_relative(self):	return self.vehicle.location.global_relative_frame

	def get_location_local_frame(self): 	return self.vehicle.location.local_frame

	def get_attitude(self):                 return self.vehicle.attitude

	def get_velocity(self):                 return self.vehicle.velocity

	def get_gps(self):                      return self.vehicle.gps_0

	def get_heading(self):                  return self.vehicle.heading

	def is_armable(self):                   return self.vehicle.is_armable

	def get_system_status(self):    		return self.vehicle.system_status.state

	def get_groundspeed(self):      		return self.vehicle.groundspeed

	def get_airspeed(self):         		return self.vehicle.airspeed

	def get_mode(self):                 	return self.vehicle.mode.name

	def get_home_location(self):        	return self.vehicle.home_location

	def get_battery_voltage(self):          return self.vehicle.battery.voltage
	
	def get_battery_current (self):         return self.vehicle.battery.current
	
	def get_battery_level (self):           
		if self.vehicle.battery.level is None:
			return -1
		return self.vehicle.battery.level

	
	def get_distance_metres(aLocation1, aLocation2):
		dlat        = aLocation2.lat - aLocation1.lat
		dlong       = aLocation2.lon - aLocation1.lon
		return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5



		
	##############################################
	#				PRINTS						 #
	##############################################
	
	def print_vehicle_state(self):
		print '|  Pitch: $%.2f  |  Yaw: $%.2f  |  Roll: $%.2f  |  Heading: $%.2f  |' % (self.vehicle.attitude.pitch, self.vehicle.attitude.yaw, self.vehicle.attitude.roll, self.vehicle.heading)
		
		
	def print_vehicle_info(self):
		print "Attitude"
		print "========"
		print 'pitch: $%.2f' % (self.vehicle.attitude.pitch) 
		print 'yaw:   $%.2f' % (self.vehicle.attitude.yaw) 
		print 'roll:  $%.2f' % (self.vehicle.attitude.roll)
		print ' '
		#print 'Battery'
		#print '======='
		#print 'Voltage: $%.2f' % (self.vehicle.battery.voltage)
		#print 'Current: $%.2f' % (self.vehicle.battery.current)
		#print 'Level:   $%.2f' % (self.vehicle.battery.level)
		
		
	def print_vehicle_full_state_info(self):
		# Get all vehicle attributes (state)
		print "\nGet all vehicle attribute values:"
		print " Global Location: ...................... %s" % self.vehicle.location.global_frame
		print " Global Location (relative altitude): .. %s" % self.vehicle.location.global_relative_frame
		print " Local Location: ....................... %s" % self.vehicle.location.local_frame
		print " Attitude: ............................. %s" % self.vehicle.attitude
		print " Velocity: ............................. %s" % self.vehicle.velocity
		print " GPS: .................................. %s" % self.vehicle.gps_0
		print " Gimbal status: ........................ %s" % self.vehicle.gimbal
		print " Battery: .............................. %s" % self.vehicle.battery
		print " EKF OK?: .............................. %s" % self.vehicle.ekf_ok
		print " Last Heartbeat: ....................... %s" % self.vehicle.last_heartbeat
		print " Rangefinder: .......................... %s" % self.vehicle.rangefinder
		print " Rangefinder distance: ................. %s" % self.vehicle.rangefinder.distance
		print " Rangefinder voltage: .................. %s" % self.vehicle.rangefinder.voltage
		print " Heading: .............................. %s" % self.vehicle.heading
		print " Is Armable?: .......................... %s" % self.vehicle.is_armable
		print " System status: ........................ %s" % self.vehicle.system_status.state
		print " Groundspeed: .......................... %s" % self.vehicle.groundspeed	# settable
		print " Airspeed: ............................. %s" % self.vehicle.airspeed		# settable
		print " Mode: ................................. %s" % self.vehicle.mode.name    # settable
		print " Armed: ................................ %s" % self.vehicle.armed		# settable
		print "\n \n"
		
	##############################################
	#				VEHICLE						 #
	##############################################
	
	# Loof until the drone is initialise
	def vehicle_pre_arm_check(self):
		while not self.vehicle.is_armable:
			print " Waiting for vehicle to initialise..."
			time.sleep(1)
	
	# Start to arm the motors
	def vehicle_arm(self):
		print "==> Vehicle Start Arming"
		self.vehicle.mode = VehicleMode("GUIDED")	# Copter should arm in GUIDED mode
		self.vehicle.armed = True
		return 1

	# Loof until the the motors are armed
	def vehicle_arming_check(self):
		while not self.vehicle.armed:
			print "==> Waiting for vehicle to arm"
			time.sleep(1)
			#self.vehicle.armed = True
	
	# Taking off the drone to the given altitude - Loof until the the drone reaches the altitude
	def vehicle_take_off(self, takeOffAltitude):
		print "Vehicle Taking Off!"
		self.vehicle.simple_takeoff(takeOffAltitude) # Take off to target altitude

		# Wait until the vehicle reaches a safe height before processing the goto
		while True:
			print " Altitude: ", self.vehicle.location.global_relative_frame.alt	  
			if self.vehicle.location.global_relative_frame.alt >= takeOffAltitude*0.95: #Trigger just below target alt.
				print "Reached target altitude"
				break
			time.sleep(1)
			
	# Take the drone to the specifide location, 
	def simpleGoTo(self, lat, lng, alt, velocity = -1):
		#dest = LocationGlobalRelative(lat, lon, height)
		# set the default travel speed
		if velocity == -1:
			self.vehicle.airspeed = 1
		else:
			self.vehicle.airspeed = velocity
		
		dest = LocationGlobalRelative(lat, lng, alt)
		self.vehicle.simple_goto(dest)
		
	
	def vehicle_RTL(self):
		self.vehicle.mode = VehicleMode("RTL")
		self.vehicle.flush()
			
	# Take the drone to 
	def vehicle_goto_location(self, location):
		currentLocation = self.vehicle.location
		targetDistance = get_distance_metres(currentLocation, location)
		gotoFunction(location);
		self.vehicle.flush()
		while not api.exit and self.vehicle.mode.name=="GUIDED": #Stop action if we are no longer in guided mode.
			remainingDistance = get_distance_metres(self.vehicle.location, location)
			if remainingDistance <= targetDistance * 0.01: #Just below target, in case of undershoot.
				print "Reached target"
				break;
			time.sleep(2)

			
	def vehicle_condition_yaw(self, heading, relative=False):
		"""
			Send MAV_CMD_CONDITION_YAW message to point vehicle at a specified heading (in degrees).
			This method sets an absolute heading by default, but you can set the `relative` parameter
			to `True` to set yaw relative to the current yaw heading.
			By default the yaw of the vehicle will follow the direction of travel. After setting 
			the yaw using this function there is no way to return to the default yaw "follow direction 
			of travel" behaviour
		"""
		
		if relative:
			is_relative=1 #yaw relative to direction of travel
		else:
			is_relative=0 #yaw is an absolute angle
		# create the CONDITION_YAW command using command_long_encode()
		msg = self.vehicle.message_factory.command_long_encode(
			0, 0,        # target system, target component
			mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
			0, 			 #confirmation
			heading,     # param 1, yaw in degrees
			0,           # param 2, yaw speed deg/s
			1,           # param 3, direction -1 ccw, 1 cw
			is_relative, # param 4, relative offset 1, absolute angle 0
			0, 0, 0)     # param 5 ~ 7 not used
		
		# send command to vehicle
		self.vehicle.send_mavlink(msg)
	
	
	
	def vehicle_rotate_camera_gimbal(self, location):
		"""
			Send MAV_CMD_DO_SET_ROI message to point camera gimbal at a 
			specified region of interest (LocationGlobal).
			The vehicle may also turn to face the ROI.
		"""
		
		# create the MAV_CMD_DO_SET_ROI command
		msg = self.vehicle.message_factory.command_long_encode(
			0, 0,    # target system, target component
			mavutil.mavlink.MAV_CMD_DO_SET_ROI, #command
			0, #confirmation
			0, 0, 0, 0, #params 1-4
			location.lat,
			location.lon,
			location.alt
			)
		# send command to vehicle
		self.vehicle.send_mavlink(msg)
		
		
		
		
		
		
	"""
		Functions to make it easy to convert between the different frames-of-reference. In particular these
		make it easy to navigate in terms of "metres from the current position" when using commands that take 
		absolute positions in decimal degrees.
		The methods are approximations only, and may be less accurate over longer distances, and when close 
		to the Earth's poles.
		Specifically, it provides:
		* get_location_metres - Get LocationGlobal (decimal degrees) at distance (m) North & East of a given LocationGlobal.
		* get_distance_metres - Get the distance between two LocationGlobal objects in metres
		* get_bearing - Get the bearing in degrees to a LocationGlobal
	"""

	def get_location_metres(original_location, dNorth, dEast):
		"""
		Returns a LocationGlobal object containing the latitude/longitude `dNorth` and `dEast` metres from the 
		specified `original_location`. The returned LocationGlobal has the same `alt` value
		as `original_location`.
		The function is useful when you want to move the vehicle around specifying locations relative to 
		the current vehicle position.
		The algorithm is relatively accurate over small distances (10m within 1km) except close to the poles.
		"""
		earth_radius=6378137.0 #Radius of "spherical" earth
		#Coordinate offsets in radians
		dLat = dNorth/earth_radius
		dLon = dEast/(earth_radius*math.cos(math.pi*original_location.lat/180))

		#New position in decimal degrees
		newlat = original_location.lat + (dLat * 180/math.pi)
		newlon = original_location.lon + (dLon * 180/math.pi)
		if type(original_location) is LocationGlobal:
			targetlocation=LocationGlobal(newlat, newlon,original_location.alt)
		elif type(original_location) is LocationGlobalRelative:
			targetlocation=LocationGlobalRelative(newlat, newlon,original_location.alt)
		else:
			raise Exception("Invalid Location object passed")
			
		return targetlocation;


	def get_distance_metres(aLocation1, aLocation2):
		"""
		Returns the ground distance in metres between two LocationGlobal objects.
		This method is an approximation, and will not be accurate over large distances and close to the 
		"""
		dlat = aLocation2.lat - aLocation1.lat
		dlong = aLocation2.lon - aLocation1.lon
		return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5


	def get_bearing(aLocation1, aLocation2):
		"""
		Returns the bearing between the two LocationGlobal objects passed as parameters.
		This method is an approximation, and may not be accurate over large distances and close to the 
		earth's poles.
		"""	
		off_x = aLocation2.lon - aLocation1.lon
		off_y = aLocation2.lat - aLocation1.lat
		bearing = 90.00 + math.atan2(-off_y, off_x) * 57.2957795
		if bearing < 0:
			bearing += 360.00
		return bearing;



	"""
	Functions to move the vehicle to a specified position (as opposed to controlling movement by setting velocity components).
	The methods include:
	* goto_position_target_global_int - Sets position using SET_POSITION_TARGET_GLOBAL_INT command in 
		MAV_FRAME_GLOBAL_RELATIVE_ALT_INT frame
	* goto_position_target_local_ned - Sets position using SET_POSITION_TARGET_LOCAL_NED command in 
		MAV_FRAME_BODY_NED frame
	* goto - A convenience function that can use Vehicle.simple_goto (default) or 
		goto_position_target_global_int to travel to a specific position in metres 
		North and East from the current location. 
		This method reports distance to the destination.
	"""

	def goto_position_target_global_int(aLocation):
		"""
		Send SET_POSITION_TARGET_GLOBAL_INT command to request the vehicle fly to a specified LocationGlobal.
		See the above link for information on the type_mask (0=enable, 1=ignore). 
		At time of writing, acceleration and yaw bits are ignored.
		"""
		msg = self.vehicle.message_factory.set_position_target_global_int_encode(
			0,       # time_boot_ms (not used)
			0, 0,    # target system, target component
			mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, # frame
			0b0000111111111000, # type_mask (only speeds enabled)
			aLocation.lat*1e7, # lat_int - X Position in WGS84 frame in 1e7 * meters
			aLocation.lon*1e7, # lon_int - Y Position in WGS84 frame in 1e7 * meters
			aLocation.alt, # alt - Altitude in meters in AMSL altitude, not WGS84 if absolute or relative, above terrain if GLOBAL_TERRAIN_ALT_INT
			0, # X velocity in NED frame in m/s
			0, # Y velocity in NED frame in m/s
			0, # Z velocity in NED frame in m/s
			0, 0, 0, # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
			0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink) 
		# send command to vehicle
		self.vehicle.send_mavlink(msg)



	def goto_position_target_local_ned(north, east, down):
		"""	
		Send SET_POSITION_TARGET_LOCAL_NED command to request the vehicle fly to a specified 
		location in the North, East, Down frame.
		It is important to remember that in this frame, positive altitudes are entered as negative 
		"Down" values. So if down is "10", this will be 10 metres below the home altitude.
		Starting from AC3.3 the method respects the frame setting. Prior to that the frame was
		ignored. For more information see: 
		http://dev.ardupilot.com/wiki/copter-commands-in-guided-mode/#set_position_target_local_ned
		See the above link for information on the type_mask (0=enable, 1=ignore). 
		At time of writing, acceleration and yaw bits are ignored.
		"""
		msg = self.vehicle.message_factory.set_position_target_local_ned_encode(
			0,       # time_boot_ms (not used)
			0, 0,    # target system, target component
			mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
			0b0000111111111000, # type_mask (only positions enabled)
			north, east, down, # x, y, z positions (or North, East, Down in the MAV_FRAME_BODY_NED frame
			0, 0, 0, # x, y, z velocity in m/s  (not used)
			0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
			0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink) 
		# send command to vehicle
		self.vehicle.send_mavlink(msg)
		
		
	def send_ned_velocity(velocity_x, velocity_y, velocity_z, duration):
		"""
		Move vehicle in direction based on specified velocity vectors and
		for the specified duration.
		This uses the SET_POSITION_TARGET_LOCAL_NED command with a type mask enabling only 
		velocity components 
		(http://dev.ardupilot.com/wiki/copter-commands-in-guided-mode/#set_position_target_local_ned).
		
		Note that from AC3.3 the message should be re-sent every second (after about 3 seconds
		with no message the velocity will drop back to zero). In AC3.2.1 and earlier the specified
		velocity persists until it is canceled. The code below should work on either version 
		(sending the message multiple times does not cause problems).
		
		See the above link for information on the type_mask (0=enable, 1=ignore). 
		At time of writing, acceleration and yaw bits are ignored.
		"""
		msg = self.vehicle.message_factory.set_position_target_local_ned_encode(
			0,       # time_boot_ms (not used)
			0, 0,    # target system, target component
			mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
			0b0000111111000111, # type_mask (only speeds enabled)
			0, 0, 0, # x, y, z positions (not used)
			velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
			0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
			0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink) 

		# send command to vehicle on 1 Hz cycle
		for x in range(0,duration):
			self.vehicle.send_mavlink(msg)
			time.sleep(1)
		
    


	def send_global_velocity(velocity_x, velocity_y, velocity_z, duration):
		"""
		Move vehicle in direction based on specified velocity vectors.
		This uses the SET_POSITION_TARGET_GLOBAL_INT command with type mask enabling only 
		velocity components 
		(http://dev.ardupilot.com/wiki/copter-commands-in-guided-mode/#set_position_target_global_int).
		
		Note that from AC3.3 the message should be re-sent every second (after about 3 seconds
		with no message the velocity will drop back to zero). In AC3.2.1 and earlier the specified
		velocity persists until it is canceled. The code below should work on either version 
		(sending the message multiple times does not cause problems).
		
		See the above link for information on the type_mask (0=enable, 1=ignore). 
		At time of writing, acceleration and yaw bits are ignored.
		"""
		msg = self.vehicle.message_factory.set_position_target_global_int_encode(
			0,       # time_boot_ms (not used)
			0, 0,    # target system, target component
			mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, # frame
			0b0000111111000111, # type_mask (only speeds enabled)
			0, # lat_int - X Position in WGS84 frame in 1e7 * meters
			0, # lon_int - Y Position in WGS84 frame in 1e7 * meters
			0, # alt - Altitude in meters in AMSL altitude(not WGS84 if absolute or relative)
			# altitude above terrain if GLOBAL_TERRAIN_ALT_INT
			velocity_x, # X velocity in NED frame in m/s
			velocity_y, # Y velocity in NED frame in m/s
			velocity_z, # Z velocity in NED frame in m/s
			0, 0, 0, # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
			0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink) 

		# send command to vehicle on 1 Hz cycle
		for x in range(0,duration):
			self.vehicle.send_mavlink(msg)
			time.sleep(1)    

		
		
