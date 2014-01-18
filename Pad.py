#!/usr/bin/env python

import pygame

class Joystick:
	"This class provides the tools for the Joystick utilisation in the Client interface"
	
	def __init__(self):
		"Class initialization"
		
		
		
	def runDetect(self):
		"This function help to detect if a Joystick is plugged"
		nb_joysticks = pygame.joystick.get_count()
		if nb_joysticks > 0:
			self.j = pygame.joystick.Joystick(0)
			self.j.init()
	
	def dispValues(self):
		
		"This function display the Joystick features on screen"
		pygame.init()
		pygame.joystick.init()
		nb_joysticks = pygame.joystick.get_count()
		if nb_joysticks > 0:
			mon_joystick = pygame.joystick.Joystick(0)
			mon_joystick.init()
		print("Axes :", mon_joystick.get_numaxes())
		print("Boutons :", mon_joystick.get_numbuttons())
		print("Trackballs :", mon_joystick.get_numballs())
		#print("Hats :", mon_joystick.get_numhats())
		
	def run(self):
		
		
		
		if nb_joysticks > 0:
			mon_joystick = pygame.joystick.Joystick(0)
			mon_joystick.init()
			nb_boutons = mon_joystick.get_numbuttons()
			
			if nb_boutons >= 4:
				continuer = 1
				while continuer:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							continuer = 0
						if event.type == pygame.JOYBUTTONDOWN and event.button == 0:
							print("Boum !")
			else:
				print("Votre Joystick ne possede pas au moins 4 boutons")
		else:
			print("Vous n avez pas branche de Joystick...")