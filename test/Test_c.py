#!/usr/bin/env python

import sys, os, inspect, time
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from Net import *
from Platform import *



# 0. Initialization
p = Pltf_ctl();
l1 = Led(Led.BLINK_L)
l2 = Led(Led.BLINK_M)
l3 = Led(Led.BLINK_H)
p.set_led(l1,0)
p.set_led(l2,1)
p.set_led(l3,2)
p2 = Pltf_ctl(True, Led(Led.BLINK_L), Led(Led.BLINK_M), Led(Led.BLINK_H))
n = NetToolClient('localhost', 50008);

# 1. Connection
n.connection()
time.sleep(5)

# 2. Send a message
n.send_str('Hello Raoul! Do you copy?')
time.sleep(2)

# 3. Receive a response
s = n.receive_str()
print "Response from server:", s

# 4. Send an object
n.send_obj(p)

# 5. Receive the modified object
p = n.receive_obj()
print "L1: Type: ", type(p.get_led(0).state), "  Val: ", p.get_led(0).state;
print "L2: Type: ", type(p.get_led(1).state), "  Val: ", p.get_led(1).state;
print "L3: Type: ", type(p.get_led(2).state), "  Val: ", p.get_led(2).state;

# 6. Deconnection
n.deconnection();
