
# import the necessary packages
import numpy as np
import argparse
import cv2


frame = None #initialize frame
roiPts = [] #initialize ROI points array
inputMode = False # initialize mode
heading=""
pitch =""


# select object to truck by 4 points
def select_ROI(event, x, y, flags, param): ##function to select the points by pressing with the mouse on the points  
    
    global frame, roiPts, inputMode

    if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts) < 4: ## check if input mode is available and start
        roiPts.append((x, y))
        cv2.circle(frame, (x, y), 4, (0,0,255),2) #create a circle on the needed frame
        cv2.imshow("frame", frame) # show the circle on the frame
       
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def determine_ROI_for_first_time():
    
    global inputMode, roiBox, roiPts, roiHist
    
    # set input mode and copy the frame to stand still
    inputMode = True
    orig = frame.copy()

    
    while len(roiPts) < 4: #wait for 4 points to get picked
        cv2.imshow("frame", frame)
        cv2.waitKey(0)

    #set top left and buttom right points
    roiPts = np.array(roiPts)
    s = roiPts.sum(axis = 1)
    tl = roiPts[np.argmin(s)]  #top left point of object 
    br = roiPts[np.argmax(s)]  #buttom right
    
        

    # get the bounding points
    roi = orig[tl[1]:br[1], tl[0]:br[0]]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)



    roiHist = cv2.calcHist([roi], [0], None, [16], [0, 180])
    roiHist = cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
    return (tl[0], tl[1], br[0], br[1])
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_centerRoi(pts):
    global centerRoi
    
    x = ((pts[0][0]+pts[1][0]+pts[2][0]+pts[3][0])/4)
    y = ((pts[0][1]+pts[1][1]+pts[2][1]+pts[3][1])/4)
    
    centerRoi = (x,y) 
    return centerRoi

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_centerScreen(frame):
    global centerScr
    
    (h, w) = frame.shape[:2]   # center of screen
    centerScr = (w / 2, h / 2)
    return centerScr



#~~~~~~~~~~~~~~~~~~~~~~~~~~move~gimbel~up~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
def gimbel_up(centerScr):
    
    x=0
    y =(centerScr[1]*2)-75

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'move cam up',(x,y), font,1,(248,248,255),2)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~move~gimbel~down~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
def gimbel_down(centerScr):

    x=0
    y =(centerScr[1]*2)-75

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'move cam down',(x,y), font,1,(248,248,255),2)

 
#~~~~~~~~~~~~~~~~~~~~~~~~~~move~gimbel~right~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gimbel_right(centerScr):

    x=0
    y =(centerScr[1]*2)-50

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'move cam right',(x,y), font,1,(248,248,255),2)

#~~~~~~~~~~~~~~~~~~~~~~~~~~move~gimbel~left~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gimbel_left(centerScr):

    x=0
    y =(centerScr[1]*2)-50

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'move cam left',(x,y), font,1,(248,248,255),2)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~move~gimbel~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gimbel_move(pts,frame):
    global heading,pitch     
    
    centerRoi = get_centerRoi(pts)
    centerScr = get_centerScreen(frame)
    xScr = centerScr[0]
    yScr = centerScr[1]
    xRoi = centerRoi[0]
    yRoi = centerRoi[1]
    
    s = pts.sum(axis = 1)    
    tl = pts[np.argmin(s)]  #top left point of object 
    br = pts[np.argmax(s)]  #buttom right
    
    
    if xRoi > xScr:
        if abs(xRoi - xScr)>=80:    
            heading = 'Move gimbel right'
            gimbel_right(centerScr)
        else:
            heading = ''
        
    if xRoi < xScr:
        if abs(xRoi - xScr)>=80:
            heading = 'Move gimbel left'
            gimbel_left(centerScr)    
        else:
            heading = ''
            
    if yRoi > yScr:
        if abs(yRoi - yScr)>=80:    
            pitch = 'Move gimbel down'
            gimbel_down(centerScr)
        else:
            pitch = ''    
            
    if yRoi < yScr:
        if abs(yRoi - yScr)>=80:
            pitch = 'Move gimbel up'
            gimbel_up(centerScr)
        else:
            pitch = ''  
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~traget~Acquired~text~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def tragetAcquired(pts):
    
    s = pts.sum(axis = 1)    
    tl = pts[np.argmin(s)]  #top left point of object 
    br = pts[np.argmax(s)]  #buttom right
     
    if tl[0]>=0 and br[0]>=0:
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame,'Traget Acquired',(0,15), font,1,(0,0,255),1)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def lineRoiTocenter(centerRoi,centerSrc):
    cv2.line(frame,(centerRoi[0],centerRoi[1]),(centerScr[0],centerScr[1]),(0,0,255),2) # print line
   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_pitch():
    return pitch           

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_heading():
    return heading           
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~do~camshift~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def print_data():
    
    (h, w) = frame.shape[:2]   # size of screen
    
    cv2.rectangle(frame,(w-390,h-225),(w-10,h-35),(248,248,255),1)
    
    #Distance to Target
    x = w-385   
    y = h-50 
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Distance to Target:20m',(x,y), font,1,(248,248,255),1)
    
    #Heading to Target
    y = y-35
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Heading to Target:50',(x,y), font,1,(248,248,255),1)
        
    
    #vihcle Velocity
    y = y-35
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Vehicle Velocity:50',(x,y), font,1,(248,248,255),1)
    
    
    
    #vihcle Attitude 
    y = y-35
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Vehicle Attitude:3m',(x,y), font,1,(248,248,255),1)
    
    
    #vihcle heading 
    y = y-35
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Vehicle heading:180',(x,y), font,1,(248,248,255),1)
    
    
    
    
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
def do_camshift():
    global frame, roiBox
    
    # convert the current frame to the HSV color space and perform mean shift
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    backProj = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1)

    # apply cam shift to the back projection, convert the points to a bounding box, and then draw them
    (r, roiBox) = cv2.CamShift(backProj, roiBox, termination)
    pts = np.int0(cv2.boxPoints(r))
    cv2.polylines(frame, [pts], True, (0,255,0), 2)

    centerScr = get_centerScreen(frame)
    x = centerScr[0]
    y = centerScr[1]
    
    # print "+" in the center of screen
    cv2.line(frame,(x,y-10),(x,y+10),(0,0,255),2) # print line
    cv2.line(frame,(x-10,y),(x+10,y),(0,0,255),2) # print line
   # cv2.line(frame,(x,y),(x+80,y),(0,255,0),2) # print line
    
    
    centerRoi = get_centerRoi(pts)    
    x = centerRoi[0]
    y = centerRoi[1]
    
    # print "+" in the center of ROI
    cv2.line(frame,(x,y-10),(x,y+10),(0,255,0),2) # print line
    cv2.line(frame,(x-10,y),(x+10,y),(0,255,0),2) # print line
    
    gimbel_move(pts,frame)
    lineRoiTocenter(centerRoi,centerScr)
    print_data()
    
    
    tragetAcquired(pts)
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

def main():
 

    
    global frame, roiPts, inputMode, roiBox, termination#global varbs

    # grab the reference to the camera
    
    #for gopro
    #camera = cv2.VideoCapture("http://10.5.5.9:8080/live/amba.m3u8") 
    
    #for comuter camera
    #camera = cv2.VideoCapture(1)
    camera = cv2.VideoCapture("/home/idan/Desktop/v/z.mp4")
    
    # setup the mouse callback
    cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
    #cv2.namedWindow("frame")
   
    cv2.setMouseCallback("frame", select_ROI)

    # initialize the termination criteria for cam shift, indicating a maximum of ten iterations or movement by a least one pixel along with the bounding box of the ROI
    termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    roiBox = None

    
    while True: #loop the frame
        # grab the current frame
        (grabbed, frame) = camera.read()

        # handle if the 'i' key is pressed, then go into ROI selection mode
        key = cv2.waitKey(1) & 0xFF
        if key == ord("i") and len(roiPts) < 4:
            roiBox = determine_ROI_for_first_time()
        
        # checks if the ROI has been computed
        
        #print roiBox
        if roiBox is not None: #check if there are roi points
            do_camshift()
        
        # show the frame and record if the user presses a key
        cv2.imshow("frame", frame)
        
       
        if key == ord("q"): #quit on 'q'
            break

    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
