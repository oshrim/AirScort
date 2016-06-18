from Vehicle import Vehicle
from android import Android
from multiprocessing import Process
import threading 
import camshift
import time
import tests

def main():
    global loc, alt
    main.alt=1    
   
    while True:
        
        print '~~~~~~~~~~~~~~~~main~~~~~~~~~~~~~~~\n'\
              'Chose mode to run   \n'\
              's - Simultor mode   \n'\
              'r - Vihcle mode     \n'\
              't - Run tests       \n'\
              '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        userIn = raw_input()
        if userIn == 's' or userIn == 'r':
            vec =Vehicle('/dev/ttyUSB0',userIn)
            vec.arm_and_takeoff(main.alt)
            time.sleep(2)
            vec_loc = vec.get_location()
            vec.simpleGoTo(vec_loc.lat,vec_loc.lon,main.alt,-1)
            run_threads(vec)
            break      
        if userIn == 't':
            tests.main()
            break
    
    
    
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def run_threads(vec):

    p1 = threading.Thread(target=camshift.main,args=(vec,),name="1")
    p2 = threading.Thread(target=get_gps,name ="2")
    p3 = threading.Thread(target=truck_object,args=(vec,),name ="3")
    
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
def truck_object(vec):
    
    time.sleep(6)
    vec.simpleGoTo(main.loc[0],main.loc[1],main.alt,-1)
    lat_loc=main.loc[0]
    lon_loc=main.loc[1]   
    
    while True:
        if True:
            time.sleep(0.1)
            if lat_loc != main.loc[0] or lon_loc != main.loc[1]: 
                vec.simpleGoTo(main.loc[0],main.loc[1],main.alt,-1)
                print 'simplegoto'
                print main.loc
                lat_loc=main.loc[0]
                lon_loc=main.loc[1]
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_gps():
    android = Android()
    while True:
        main.loc = android.getLatAndLon()   
        #time.sleep(1) 
        
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          
def get_loc():
    return main.loc
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
if __name__ == "__main__":
    main()
    
    
    
