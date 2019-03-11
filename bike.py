#!/usr/bin/python
import numpy as np


class Bike(object):
	"""
	Minimal bike object that is passed around.
	Bike object is initialized with a NumPy array representing point location (2x4).
	"""
	
	def __init__(self, locations):
		self.locations = locations
		self.x = 0
		self.y = 1
		self.activeWheel = 0
		self.passiveWheel = 1
		self.handlebar1 = 2
		self.handlebar2 = 3
		self.distance_made = 0
		
	def __str__(self):
		return "Ring, ring, I'm a bike. :D"