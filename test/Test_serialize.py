#!/usr/bin/env python

import socket
import pickle
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from Net import *
from Platform import *



# Serialize
p = Pltf_ctl();
l1 = Led(Led.BLINK_L)
l2 = Led(Led.BLINK_M)
l3 = Led(Led.BLINK_H)
p.set_led(l1,0)
p.set_led(l2,1)
p.set_led(l3,2)
p2 = Pltf_ctl(True, Led(Led.BLINK_L), Led(Led.BLINK_M), Led(Led.BLINK_H))
s = pickle.dumps(p);
s2 = pickle.dumps(p2);

print "---BEFORE---"
print "P:  Type: ", type(p), "   Val:  ", p
print "L1: Type: ", type(p.get_led(0).state), "  Val: ", p.get_led(0).state;
print "L2: Type: ", type(p.get_led(1).state), "  Val: ", p.get_led(1).state;
print "L3: Type: ", type(p.get_led(2).state), "  Val: ", p.get_led(2).state;
print "L21: Type: ", type(p2.get_led(0).state), "  Val: ", p2.get_led(0).state;
print "L22: Type: ", type(p2.get_led(1).state), "  Val: ", p2.get_led(1).state;
print "L23: Type: ", type(p2.get_led(2).state), "  Val: ", p2.get_led(2).state;

# Deserialize
pn = pickle.loads(s)
p2n = pickle.loads(s2)
print "---AFTER---"
print "P:  Type: ", type(pn), "   Val:  ", pn
print "L1: Type: ", type(pn.get_led(0).state), "  Val: ", pn.get_led(0).state;
print "L2: Type: ", type(pn.get_led(1).state), "  Val: ", pn.get_led(1).state;
print "L3: Type: ", type(pn.get_led(2).state), "  Val: ", pn.get_led(2).state;
print "L21: Type: ", type(p2n.get_led(0).state), "  Val: ", p2n.get_led(0).state;
print "L22: Type: ", type(p2n.get_led(1).state), "  Val: ", p2n.get_led(1).state;
print "L23: Type: ", type(p2n.get_led(2).state), "  Val: ", p2n.get_led(2).state;

