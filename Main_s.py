#!/usr/bin/env python

import time, os , inspect, sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from Net import *
from Platform import *

# 0. Initialization
n = NetToolServer();

# 1. Wait for a connection
n.wait_conn();

## 2. Receive a message
#s = n.receive_str();
#print "Message from client:", s

## 3. Send a response
#n.send_str("Ok, I copy!")
#time.sleep(2)

# 4. Receive an object
while 1:
	p = n.receive_obj()
	print "Received command:  X: ", p.servo_h.speed, " et Y: ", p.servo_v.speed
	n.send_str('ACK')

## 5. Modify and resent the object
#p.led2.set_state(Led.OFF)
#p.led1.set_state(Led.ON)
#n.send_obj(p)

## 6. Deconnection
#n.deconnection()
