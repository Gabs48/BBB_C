#!/usr/bin/env python

import pygame
import sys
import Utils
import time
import datetime

class Joystick:
	"This class provides the tools for the Joystick utilisation in the Client interface"
	
	def __init__(self):
		"Class initialization"
		self.PADUNRECOGN = 0
		self.PADUSBGEN = 1
		pygame.init()
		pygame.joystick.init()
		self.choose()
		self.defType()
		
	def choose(self):
		"This function help to choose wich Joystick to use when plugged"
		nb_joysticks = pygame.joystick.get_count()
		if nb_joysticks >1:
			print "Choose which Joystick you want to use (between 1 and %d):" % nb_joysticks,
			n = input();
			self.j = pygame.joystick.Joystick(n-1)
			self.j.init()
		elif nb_joysticks == 1:
			self.j = pygame.joystick.Joystick(0)
			self.j.init()
		else:
			print "No Joystick plugged! Verify the connection and the recognition by the OS..."
			
	def defType(self):
		if self.j.get_name().find("Microntek              USB Joystick") != -1:
			self.jType = self.PADUSBGEN;
		else:
			self.jType = self.PADUNRECOGN;
	
	def dispFeatures(self):
		"This function display the Joystick features on screen"
		print "Axes :", self.j.get_numaxes()
		print "Boutons :", self.j.get_numbuttons()
		print "Trackballs :", self.j.get_numballs()
		
	def run(self):
		"This function check if there is an event on the pad. If yes, it fill the command structure, which can be send then"
		X1 = 0.0
		Y1 = 0.0
		X2 = 0.0
		Y2 = 0.0
		X3 = 0
		Y3 = 0
		while True:
			
			# Sleep is required for an optimized processor consumption
			time.sleep(0.5)
			
			# Here we can fill with the command we want, depending of the joystick features
			for event in pygame.event.get():
				if event.type == pygame.JOYBUTTONDOWN:
					if event.button == 0:
						#print "Triangle"
					elif event.button == 1:
						#print "Rond"
					elif event.button == 2:
						#print "Croix"
					elif event.button == 3:
						#print "Carre"
					elif event.button == 4:
						#print "L1"
					elif event.button == 5:
						#print "R1"
					elif event.button == 6:
						#print "L2"
					elif event.button == 7:
						#print "R2"
					elif event.button == 8:
						#print "Select"
					elif event.button == 9:
						#print "Start"
					elif event.button == 10:
						#print "Pad1"
					elif event.button == 11:
						#print "Pad2"
					else:
						#print "Unknow"
				if event.type == pygame.JOYAXISMOTION:
					X1 = self.j.get_axis(0)
					Y1 = - self.j.get_axis(1)
					X2 = self.j.get_axis(2)
					Y2 = - self.j.get_axis(3)
				if event.type == pygame.JOYHATMOTION:
					(X3, Y3) = self.j.get_hat(0)
			#print "Axe 1: X = {:>3f} et Y = {:>3f}".format(X1,Y1),
			#print "  ||  Axe 2: X = {:>3f} et Y = {:>3f}".format(X2,Y2),
			#print "  ||  Axe 3: X = {:d} et Y = {:d}".format(X3,Y3)