from Vehicle import Vehicle
from android import Android
from threading import Thread
import camshift
import time

def main():
    global loc,heading,pitch   
    
    
    
    print "~~~~~~~~~~~~~~~~main~~~~~~~~~~~~~~~~"
    
    #vec =Vehicle('/dev/ttyUSB0')
   # vec.arm_and_takeoff(3)

    
    
    thread1 = Thread(target=camshift.main)
    thread1.start()
    
    
    thread2 = Thread(target=get_gps)
    thread2.start()
    time.sleep(4)
    
    #vec.simpleGoTo(main.loc[0],main.loc[1],3,-1)
    time.sleep(1)       

   # heading = vec.get_heading()


    while True:
        #print "in while gps"
    
        #print main.loc[0]
        #print main.loc[1]
        
        h =camshift.get_heading()
        p = camshift.get_pitch()
        if h !='' or p !='' :
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        if h !='':            
            print h
        if p !='':            
            print p
        
        if True:
            time.sleep(0.2)
            #vec.altitude = 3 # in meters
            #vec.simpleGoTo(main.loc[0],main.loc[1],3,-1)
           # print 'simplegoto'

    thread1.join()
    thread2.join()


def get_gps():
    android = Android()
    while True:
        main.loc = android.getLatAndLon()     


    
if __name__ == "__main__":
    main()
    
    
    
