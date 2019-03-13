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
	
	pp.ion()
	fig = pp.figure()
	ax = fig.add_subplot(111)
	
	ax.set_xlim(0, LENGTH_STAGE)
	ax.set_ylim(0, HEIGHT_STAGE)
	
	fig_floor = draw_floor(floor)
	fig_bike = draw_bike(loc_bike)
	
	pp.draw()


def draw_floor(floor):
	fig = pp.plot(floor[0, :], floor[1, :], color='g')
	return fig


def draw_bike(loc_bike):
	fig = pp.plot(loc_bike[0, :2], loc_bike[1, :2], 'bo', loc_bike[0, 2:], loc_bike[1, 2:], 'r^', markersize=5)
	for i in range(4):
		for j in range(i, 4):
			fig = pp.plot((loc_bike[0, i], loc_bike[0, j]), (loc_bike[1, i], loc_bike[1, j]), 'k-')
	return fig


def animate(floor, locs_bike):
	for loc in locs_bike:
		draw(floor, loc)
		pp.pause(.5)
	
floor = read_np_random_surface('./random_surface.csv')
bike_locs = [Bike('random').locations for i in range(10)]
animate(floor, bike_locs)
