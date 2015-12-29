from Vehicle import Vehicle
from android import Android
import time

def main():
    
    print "main"
    android = Android()
    vec =Vehicle()
    vec.arm_and_takeoff(3)
    
    while True:
        print "in while gps"
    
        if vehicle.mode.name != "GUIDED":
            print "User has changed flight modes - aborting follow-me"
            break    
           
        loc = android.getLatAndLon()
        print loc[0]
        print loc[1]
        
        if True:
            vec.altitude = 3  
            vec.simpleGoTo(loc[0],loc[1],3,1)
            time.sleep(1)

    vec.closeVec()
    
if __name__ == "__main__":
    main()
    
    
    