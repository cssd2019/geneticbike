import numpy as np
import matplotlib.pyplot as pp
from random_surface import read_np_random_surface
from bike import Bike
from time import sleep


def draw(floor, loc_bike):
	LENGTH_STAGE = 100
	HEIGHT_STAGE = 10
	SIZE_WHEEL = .2
	SIZE_HANDLE = .1
	
	fig, ax = pp.subplots()
	
	ax.set_xlim(0, LENGTH_STAGE)
	ax.set_ylim(0, HEIGHT_STAGE)
	
	fig = draw_floor(floor)
	fig = draw_bike(loc_bike)
	
	
	# ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
	# or
	pp.show()
	#sleep(2)
	fig.clear()


def draw_floor(floor):
	fig = pp.plot(floor[0, :], floor[1, :], color='g')
	return fig


def draw_bike(loc_bike):
	fig = pp.plot(loc_bike[0, :2], loc_bike[1, :2], 'bo', loc_bike[0, 2:], loc_bike[1, 2:], 'r^', markersize=5)
	for i in range(4):
		for j in range(i, 4):
			fig = pp.plot((loc_bike[0, i], loc_bike[0, j]), (loc_bike[1, i], loc_bike[1, j]), 'k-')
	return fig


floor = read_np_random_surface('./random_surface.csv')
bike_loc = Bike('random').locations
draw(floor, bike_loc)
bike_loc[0,:] += 5
draw(floor, bike_loc)