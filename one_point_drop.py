#!/usr/bin/env python

from bike import Bike
import numpy as np
import time
from random_surface import read_np_random_surface

np.seterr(divide='ignore', invalid='ignore')

# spring constant is 5 N/m
# gravity constant is 9.8 m/s**2
# time steps are 1s
# acceleration of active wheel is 4 m/s**2
k = 500 
g = 9.8
dt = 0.1
a_Aw = 4

locations = list()

floor = read_np_random_surface('./random_surface.csv')

# mB is the moving bike 
mB = Bike("random")

# masses of points as activeWheel, passiveWheel, handle1, handle2 in kg
m = np.array([0.5, 0.5, 30, 30])

v = np.zeros((2, 1))

# initial velocities of points - that is calculated initially based on acceleration of active wheel ???
mB.locations = mB.locations[:,0:1]
mB.locations[1,:] += 1
inair = True
t = 0
locations.append(mB.locations)

# gravity applies to the bike
while inair == True:
    v[1,0] = - g * dt
    mB.locations = mB.locations + v * dt
    indexFloor = floor[0,:] == np.floor(mB.locations[0,0])
    indexCeil = floor[0,:] == np.ceil(mB.locations[0,0])
    indexEq = floor[0,:] == mB.locations[0,0]
    if np.any(indexEq):
        y_touch = floor[1,indexEq]
    else:
        y_touch = (floor[1,indexFloor] + floor[1,indexCeil]) / 2
    if y_touch + 0.001 > mB.locations[1,0] and y_touch - 0.001 < mB.locations[1,0]:
        moving = True
        inair = False
        v[1,0] = 0
        v[0,0] = a_Aw * dt
    if y_touch - 0.001 > mB.locations[1,0]:
        moving = True
        inair = False
        v[1,0] = 0
        v[0,0] = a_Aw * dt
    t = t + 1
    locations.append(mB.locations)
