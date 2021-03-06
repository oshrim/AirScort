
# import the necessary packages
import numpy as np
import argparse
import cv2


frame = None #initialize frame
roiPts = [] #initialize ROI points array
inputMode = False # initialize mode



def select_ROI(event, x, y, flags, param): ##function to select the points by pressing with the mouse on the points  
    
    global frame, roiPts, inputMode

    if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts) < 4: ## check if input mode is available and start
        roiPts.append((x, y))
        cv2.circle(frame, (x, y), 4, (0, 255, 0), 2) #create a circle on the needed frame
        cv2.imshow("frame", frame) # show the circle on the frame



def determine_ROI_for_first_time():
    
    global inputMode, roiBox, roiPts, roiHist
    
    # set input mode and copy the frame to stand still
    inputMode = True
    orig = frame.copy()

    
    while len(roiPts) < 4: #wait for 4 points to get picked
        cv2.imshow("frame", frame)
        cv2.waitKey(0)

    #set top left and button right points
    roiPts = np.array(roiPts)
    s = roiPts.sum(axis = 1)
    tl = roiPts[np.argmin(s)]
    br = roiPts[np.argmax(s)]

    # get the bounding points
    roi = orig[tl[1]:br[1], tl[0]:br[0]]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)



    roiHist = cv2.calcHist([roi], [0], None, [16], [0, 180])
    roiHist = cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
    return (tl[0], tl[1], br[0], br[1])
    



def do_camshift():
    global frame, roiBox
    
    # convert the current frame to the HSV color space and perform mean shift
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    backProj = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1)

    # apply cam shift to the back projection, convert the points to a bounding box, and then draw them
    (r, roiBox) = cv2.CamShift(backProj, roiBox, termination)
    pts = np.int0(cv2.boxPoints(r))
    cv2.polylines(frame, [pts], True, (0, 255, 0), 2)



def main():
 

    
    global frame, roiPts, inputMode, roiBox, termination #global varbs

    # grab the reference to the camera
    
    #for gopro
    #camera = cv2.VideoCapture("http://10.5.5.9:8080/live/amba.m3u8") 
    
    #for comuter camera
    camera = cv2.VideoCapture(0)
    
    
    # setup the mouse callback
    cv2.namedWindow("frame")
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
        print roiBox
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
