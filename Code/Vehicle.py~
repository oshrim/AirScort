
from dronekit import connect, VehicleMode, LocationGlobalRelative
import socket
import time
import sys



class Vehicle():
   
    def __init__(self,connectionString):
        print 'Connecting to vehicle on: %s' % connectionString
        self.vehicle=connect(connectionString, baud=57600)
    
    def arm_and_takeoff(self,aTargetAltitude):
        """
        Arms vehicle and fly to aTargetAltitude.
        """
   
        time.sleep(1)

        
        print "Arming motors"
        # Copter should arm in GUIDED mode
        self.vehicle.mode    = VehicleMode("GUIDED")
        self.vehicle.armed   = True    

        while not vehicle.armed:      
            print " Waiting for arming..."
            time.sleep(1)

        print "Taking off!"
        self.vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command 
    #  after Vehicle.simple_takeoff will execute immediately).
        while True:
            print " Altitude: ", self.vehicle.location.global_relative_frame.alt      
            if self.vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: #Trigger just below target alt.
                print "Reached target altitude"
                break
            time.sleep(1)
            
    def air_speed(self,speed):
        self.vehicle.airspeed=speed
        
    def simpleGoTo(self,lat,lon,height,groundSpeed =-1):
        dest = LocationGlobalRelative(lat, lon, height)
        if groundSpeed == -1:
            self.vehicle.simple_goto(dest)
        else:
            self.vehicle.simple_goto(dest,groundspeed = groundSpeed)
            
    def rtl(self):
        self.vehicle.mode = VehicleMode("RTL")
    
    def closeVec(self):
        self.vehicle.close()
    
    def get_location_global_frame(self): 

        return vehicle.location.global_frame

    def get_location_global_relative_frame(self):
    
        return vehicle.location.global_relative_frame

    def get_location_local_frame(self):
    
        return vehicle.location.local_frame

    def get_attitude(self):
    
        return vehicle.attitude

    def get_velocity(self):
    
        return vehicle.velocity

    def get_gps(self):

        return vehicle.gps_0

    def get_battery(self):
    
        return vehicle.battery

    def get_heading(self):
    
        return vehicle.heading

    def is_armable(self):
    
        return vehicle.is_armable


    def get_system_status(self):

        return vehicle.system_status.state


    def get_groundspeed(self):
        
        return vehicle.groundspeed


    def set_groundspeed(self,speed):
        vehicle.groundspeed= speed
        return
    
    def get_airspeed(self):
    
        return vehicle.airspeed


    def get_mode(self):
    
        return vehicle.mode.name

    def set_mode(self,mode):

        vehicle.mode=mode
    

    def set_armed(self,bool):
    
        vehicle.armed =bool
            
