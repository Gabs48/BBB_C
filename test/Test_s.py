#!/usr/bin/env python

import time, os , inspect, sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from Net import *
from Platform import *



# 0. Initialization
n = NetToolServer(50008);

# 1. Wait for a connection
n.wait_conn();

# 2. Receive a message
s = n.receive_str();
print "Message from client:", s

# 3. Send a response
n.send_str("Ok, I copy!")
time.sleep(2)

# 4. Receive an object
p = n.receive_obj()
print "L1: Type: ", type(p.get_led(0).state), "  Val: ", p.get_led(0).state;
print "L2: Type: ", type(p.get_led(1).state), "  Val: ", p.get_led(1).state;
print "L3: Type: ", type(p.get_led(2).state), "  Val: ", p.get_led(2).state;

# 5. Modify and resent the object
p.led2.set_state(Led.OFF)
p.led1.set_state(Led.ON)
n.send_obj(p)

# 6. Deconnection
n.deconnection()
