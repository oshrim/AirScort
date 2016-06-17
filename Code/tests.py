from Vehicle import Vehicle
from android import Android





        
def run_tests(vec):    
    print "\n------------------------------vehicle-state---------------------------------"
    print "Global Location:\n%s"                     % vec.get_location()
    
    print "Global Location (relative altitude):\n%s\n" % vec.get_location_global_relative()
  
    print "Local Location:\n%s"  % vec.get_location_local_frame()

    print "Attitude: %s" % vec.get_attitude()
  
    print "Velocity: %s" % vec.get_velocity
 
    print "GPS: %s             " % vec.get_gps()
   
    print "Battery: %s         " % vec.get_battery_level()
   
    print "Heading: %s         " % vec.get_heading()
   
    print "Is Armable?: %s     " % vec.is_armable()
    
    print "System status: %s   " % vec.get_system_status()
    
    print "Groundspeed: %s " % vec.get_groundspeed()    # settable
   
    print "Airspeed: %s " % vec.get_airspeed()    # settable
    
    print "Mode: %s\n" % vec.get_mode()    # settable
   




def main():
 
 while True:
        
        print '~~~~~~~~~~~~~~~~Run~tests~~~~~~~~~~~~~~\n'\
              'Chose mode to test:   \n'\
              's - Simultor mode   \n'\
              'r - Vihcle mode     \n'\
              '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        userIn = raw_input()
        if userIn == 's' or userIn == 'r':
            vec =Vehicle('/dev/ttyUSB0',userIn)
            run_tests(vec)       
            break      
 

if __name__ == "__main__":
    main()
    