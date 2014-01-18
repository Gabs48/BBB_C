#!/usr/bin/env python

import multiprocessing
import Gui
import Pad
import os
import subprocess



#def run_net():
	


if __name__ == '__main__':
	#p1 = multiprocessing.Process(target=run_net)
	#p1.start()
	#gui = Gui.MainWindow();
	#gui.run();
	pad = Pad.Joystick();
	pad.dispFeatures();
	pad.run()