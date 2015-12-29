# import the necessary packages
import cv2
import numpy as np
import time
from goprohero import GoProHero



class gopro:

    def connect_cam(self,Password):
    
        camera = GoProHero(password=Password)
    
        
    def set_command(self,command,conditon):
        camera.command(command,condition)
        

    def rec_on(self):
        camera.command('record', 'on')

    def rec_off(self):
        camera.command('record', 'off')
    
    def delete_all(self):
        
        camera.command('delete_all')
