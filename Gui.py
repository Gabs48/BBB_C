#!/usr/bin/env python

from Tkinter import *
from PIL import Image, ImageTk
from Net import *
import threading
import StringIO

class MainWindow(Frame):
	"This class provides a Graphical User Interface to the userwho want to pilot the robot. It uses the original Python graphic library Tkinter."
	
	def __init__(self):
		"Constructor"
		self.root = Tk()
		self.root.geometry("%dx%d+0+0" % (640, 480))
		self.root.resizable(False,False)
		self.root.title("iRobotique Client Software")
		self.addFrame()
	def addFrame(self):
		frame = Frame(self.root,  background="#FFFFFF")
		self.addCanvas(frame)
		frame.pack(fill=BOTH, expand=YES)

	def addCanvas(self, frame):
		self.canvas = Canvas(frame, background='#000000')
		self.canvas.pack(fill=BOTH, expand=YES)
		self.canvas.pack()
		
	def addImage(self, photoimage):
		self.canvas.create_image(640,480, image=photoimage,anchor=SE)

	def updateGui(self):
		"Update the video stream with a new image"
		f = get_video_stream('10.42.0.42',8080,'/?action=snapshot')
		img = Image.open(StringIO.StringIO(f))
		imagetk = ImageTk.PhotoImage(img)
		self.addImage(imagetk)
		self.root.update()
		
	def run(self):
		"Run the GUI"
		while True:
			self.updateGui()
	
	def stop(self):
		self.root.quit()