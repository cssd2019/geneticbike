import matplotlib.pyplot as pp
from random_surface import read_np_random_surface
from bike import Bike


def _draw(floor, loc_bike):
	"""
	Draws current position of the bike along with the floor.
	:param floor: Numpy array of floor (0-th column is x-axis)
	:param loc_bike: Numpy array containing current location of bike
	:return: No return value
	"""
	LENGTH_STAGE = 100
	HEIGHT_STAGE = 10
	SIZE_WHEEL = .2
	SIZE_HANDLE = .1
	
	pp.ion()
	fig = pp.figure()
	ax = fig.add_subplot(111)
	
	ax.set_xlim(0, LENGTH_STAGE)
	ax.set_ylim(0, HEIGHT_STAGE)
	
	fig_floor = _draw_floor(floor)
	fig_bike = _draw_bike(loc_bike)
	
	pp.draw()


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
		_draw(floor, loc)
		pp.pause(.5)


def testrun():
	floor = read_np_random_surface('./random_surface.csv')
	bike_locs = [Bike('random').locations for i in range(10)]
	animate(floor, bike_locs)
