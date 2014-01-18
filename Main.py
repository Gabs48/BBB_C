#!/usr/bin/env python

import multiprocessing
import Gui
import Pad



#def run_net():
	


if __name__ == '__main__':
	#p1 = multiprocessing.Process(target=run_net)
	#p1.start()
	#gui = Gui.MainWindow();
	#gui.run();
	j = Pad.Joystick();
	j.dispValues()
	