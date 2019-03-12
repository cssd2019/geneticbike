#!/usr/bin/python
import numpy as np


class Bike(object):
	"""
	Minimal bike object that is passed around.
	Bike object is initialized with a NumPy array representing point location (2x4).
	"""
	
	def __init__(self, locations):
		"""
		Initializes Bike object.
		:param locations: (2,4) Numpy array with coordinates of activeWheel, passiveWheel, handlebar1, and handlebar2.
							Single coordinates on a scale from 0 to 1.
							If set to string "random" will randomize bike coordinates.
		"""
		if type(locations) == np.ndarray:
			if locations.shape == (2, 4):
				self.locations = locations
			else:
				raise AttributeError('Wrong size for array. Array should be (2,4) but is ({}).'.format(locations.shape))
		elif locations == 'random':
			self.locations = np.random.rand(2, 4)
		else:
			raise AttributeError('Locations argument needs to be (2,4) numpy array or string "random".')
		self.x = 0
		self.y = 1
		self.activeWheel = 0
		self.passiveWheel = 1
		self.handlebar1 = 2
		self.handlebar2 = 3
		self.distance_made = None # easier to find errors if initialized to None
		
	def __str__(self):
		return "Ring, ring, I'm a bike. :D"