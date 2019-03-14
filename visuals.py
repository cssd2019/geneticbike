import matplotlib.pyplot as pp
from random_surface import read_np_random_surface
from bike import Bike


def _draw_init():
	"""
	Initializes drawing environment.
	:return: No return value
	"""
	LENGTH_STAGE = 100
	HEIGHT_STAGE = 10
	
	pp.ion()
	fig = pp.figure()
	ax = fig.add_subplot(111)
	
	ax.set_xlim(0, LENGTH_STAGE)
	ax.set_ylim(0, HEIGHT_STAGE)


def _draw_floor(floor):
	"""
	Draws the floor.
	:param floor: Floor as in draw function.
	:return: Figure object
	"""
	fig = pp.plot(floor[0, :], floor[1, :], color='g')
	return fig


def _draw_bike(loc_bike):
	"""
	Draws the bike.
	:param loc_bike: Bike as in draw function.
	:return: Figure object
	"""
	#SIZE_WHEEL = .2
	#SIZE_HANDLE = .1
	fig = pp.plot(loc_bike[0, :2], loc_bike[1, :2], 'bo', loc_bike[0, 2:], loc_bike[1, 2:], 'r^', markersize=5)
	for i in range(4):
		for j in range(i, 4):
			fig = pp.plot((loc_bike[0, i], loc_bike[0, j]), (loc_bike[1, i], loc_bike[1, j]), 'k-')
	return fig


def animate(floor, locs_bike):
	"""
	Iteratively calls draw and pauses on all the bike locations.
	:param floor: Numpy array of floor (0-th column is x-axis)
	:param locs_bike: List of Numpy arrays containing current location of bike.
	:return: Nothing
	"""
	for loc in locs_bike:
		_draw_init()
		_draw_floor(floor)
		fig = _draw_bike(loc)
		pp.pause(.1)
		pp.clf()

def testrun():
	floor = read_np_random_surface('./random_surface.csv')
	bike_locs = [Bike('random').locations for i in range(20)]
	animate(floor, bike_locs)

#testrun()
