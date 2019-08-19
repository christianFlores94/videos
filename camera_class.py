#!/usr/bin/env python3

import cv2
import numpy as np
import os
import datetime
import time
import multiprocessing as mp
import sys



class Camera:
	#constructor of the camera
	def __init__ (self, ipAdress, videoResolution):
		self.__ip = ipAdress #camera ip adress 
		self.__font = cv2.FONT_HERSHEY_SIMPLEX #font used in the camera
		self.videoRes = videoResolution
		# standar video dimensions
		self.__STD_DIMENSIONS = {
    		"480p": (640, 480),
    		"720p": (1280, 720),
    		"1080p": (1920, 1080),
    		"4k": (3840, 2160),
			}
		self.__VIDEO_TYPE = {
    		'avi': cv2.VideoWriter_fourcc(*'XVID'),
    		'mp4': cv2.VideoWriter_fourcc(*'XVID')
			}


	

	#shows the camera´s ip	
	def show_ip(self):
		return self.__ip 
	#shows the video resolution 
	def show_resolution(self):
		return self.videoRes
	def show_font(self):
		return self.__font	

	def create_TimeStamp(self):
		return '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())	

	# set resolution for video
	def change_res(self,cap, width, height):
		cap.set(3, width)
		cap.set(4, height)	
    #get video type
	def get_video_type(self,filename):
		filename, ext = os.path.splitext(filename)
		if ext in self.__VIDEO_TYPE:
			return self.__VIDEO_TYPE[ext]
		return self.__VIDEO_TYPE['avi'] 	


	def get_dims(self,cap,res):
		width, height = self.__STD_DIMENSIONS['720p']
		if res in self.__STD_DIMENSIONS:
			widths, height = self.__STD_DIMENSIONS[res]
		self.change_res(cap, width, height)
		return width, height	

	def rec(self):
		cap = cv2.VideoCapture('rtsp://' + self.show_ip() + '/')
		dims = self.get_dims(cap, res='720p')
		filename = self.create_TimeStamp() + '.avi'
		video_type_cv2 = self.get_video_type(filename)
		frames_per_seconds = 14
		
		
		out = cv2.VideoWriter(filename, video_type_cv2, frames_per_seconds, dims)

		while True:
			# capture frame
			ret, frame = cap.read()
			#create timeStamp
			actualDateAndTime = self.create_TimeStamp()
			#printing timeStamp
			cv2.putText(frame, actualDateAndTime, (0,653), self.show_font(), 1, (204,1,1), 2, cv2.LINE_AA)
			out.write(frame)
			cv2.imshow('Actual_View', frame)
			# display the resulting frame
			k = cv2.waitKey(10) & 0xFF
			if k == 27:
				break
		cap.release()
		out.release()
		cv2.destroyAllWindows()


	def rec_for(self, seconds):
		recording = mp.Process(target= self.rec)
		recording.start()
		seconds += 15
		for x in range(0,seconds):
			time.sleep(1)
		recording.terminate()		



camera1 = Camera('192.168.0.12','720p')
print(camera1.show_ip())
print(camera1.show_resolution()) 
minutes = int(sys.argv[1])
file1 = open("results.txt","w") 
camera1.rec_for(60*minutes)
file1.write("La cámara grabó por " + str(minutes) + " Minutos") 
os.system("./shellcontrol.py")

		



