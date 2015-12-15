from dronekit import connect, VehicleMode, LocationGlobalRelative
import time


#connect to vehicle with telmetry

vehicle=connect('/dev/ttyUSB0', baud=57600)


"""
this progarm controll the vehicle and take off to alltitude 3 meter

"""
def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print "Basic pre-arm checks"
    # Don't let the user try to arm until autopilot is ready
   # while not vehicle.is_armable:
    #    print " Waiting for vehicle to initialise..."
    time.sleep(2)

   #change to Guided mood : this mood allows us to send commands to vehicle         
    print "Arming motors"
    vehicle.mode = VehicleMode("GUIDED")
    
    #armed vehicle
    vehicle.armed   = True    

    while not vehicle.armed:      
        print " Waiting for arming..."
        time.sleep(1)

    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude
   # vehicle.mode = VehicleMode("GUIDED")
    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command 
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt 
        #Break and return from function just below target altitude.        
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
            print "Reached target altitude"
         
        time.sleep(1)

arm_and_takeoff(3) # set altitude to 3 meter







