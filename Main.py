#!/usr/bin/env python

from Gui import *
from Pad import *
from Platform import *
import threading, time


class Com(threading.Thread):
	"This class intends to manage the main computation"
	
	def __init__(self, pltf_):
		"Class initialization"
		threading.Thread.__init__(self)
		self.isTerminated = False
		self.pltf = pltf_
		self.net = NetToolClient('10.42.0.42')
		self.net.connection()
	
	def run(self):
		"Run the thread"
		while not self.isTerminated:
			time.sleep(0.05)
			if pltf_ctl.modif==True:
				# Send
				print "Send command:  X: ", self.pltf.servo_h.speed, " et Y: ", self.pltf.servo_v.speed
				self.net.send_obj(self.pltf)
				
				# Wait for an ACK
				ack = self.net.receive_str()
				
				# Notify the modification
				if ack=='ACK':
					print "recu"
					self.pltf.modif = False
				else:
					print "pas recu"
					
	def stop(self):
		"Stop the thread"
		self.isTerminated = True;



if __name__ == '__main__':
	"This main function launch every threads and manage exceptions"
	
	# Initialization
	pltf_state = Pltf_state()
	pltf_ctl = Pltf_ctl()

	# Launch Joystick Thread
	joystick = Joystick(pltf_ctl)
	joystick.start()
	
	# Launch Main Thread
	com = Com(pltf_ctl)
	com.start()
	
	# Launch Gui (according to tkinter library. Gui MUST be the main process, otherwise it doesn't work)
	gui = MainWindow()
	try:
		gui.run()
	except KeyboardInterrupt:
		joystick.stop()
		gui.stop()
		com.stop()
		
		