#!/usr/bin/env python

from bike import Bike
import numpy as np
import time
import sys
np.seterr(divide='ignore', invalid='ignore')

def length_calculation(mB):
#    l = np.zeros((4,4))
    l = np.zeros((2,2))
    l[0,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,0])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,0])))
    l[1,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,1])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,1])))
#    l[2,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,2])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,2])))
#    l[3,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,3])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,3])))
    return l

# spring constant is 5 N/m
# gravity constant is 9.8 m/s**2
# time steps are 1s
# acceleration of active wheel is 4 m/s**2
k = 500 
g = 9.8
dt = 0.1
a_Aw = 0.4

floor = np.random.rand(2,10)
floor[0,:] = np.array([0,1,2,3,4,5,6,7,8,9])
locations = list()

# mB is the moving bike 
mB = Bike("random")

# masses of points as activeWheel, passiveWheel, handle1, handle2 in kg
m = np.array([0.5, 0.5, 30, 30])

v = np.zeros((2, 2))

mB.locations = mB.locations[:,0:2]
mB.locations[1,:] += 1
inair_firstPoint = True
inair_secondPoint = True
t = 0
locations.append(mB.locations)

# gravity applies to the bike

# touch point for point 1
indexFloor = floor[0,:] == np.floor(mB.locations[0,0])
indexCeil = floor[0,:] == np.ceil(mB.locations[0,0])
indexEq = floor[0,:] == mB.locations[0,0]
if np.any(indexEq):
    y_touch_1 = floor[1,indexEq]
else:
    y_touch_1 = (floor[1,indexFloor] + floor[1,indexCeil]) / 2

# touch point for point 2
indexFloor = floor[0,:] == np.floor(mB.locations[0,1])
indexCeil = floor[0,:] == np.ceil(mB.locations[0,1])
indexEq = floor[0,:] == mB.locations[0,1]
if np.any(indexEq):
    y_touch_2 = floor[1,indexEq]
else:
    y_touch_2 = (floor[1,indexFloor] + floor[1,indexCeil]) / 2

v[1,:] = - g * dt

while inair_firstPoint == True or inair_secondPoint == True:
    mB.locations = mB.locations + v * dt
    if y_touch_1 + 0.001 > mB.locations[1,0] and y_touch_1 - 0.001 < mB.locations[1,0] and inair_firstPoint == True:
        moving = True
        inair_firstPoint = False
        v[1,0] = 0
    if y_touch_1 - 0.001 > mB.locations[1,0]:
        moving = True
        inair_firstPoint = False
        v[1,0] = 0

    if y_touch_2 + 0.001 > mB.locations[1,1] and y_touch_2 - 0.001 < mB.locations[1,1] and inair_secondPoint == True:
        moving = True
        inair_secondPoint = False
        v[1,1] = 0
    if y_touch_2 - 0.001 > mB.locations[1,1]:
        moving = True
        inair_secondPoint = False
        v[1,1] = 0
    t += 1
    locations.append(mB.locations)
    print(mB.locations)
    print(t)


# the initial length of springs are set here
linit = length_calculation(mB)

l = linit

v[0,:] = a_Aw * dt

# movement starts
F = np.zeros((2,2))
while moving == True:
    dx = np.zeros((2,2))
    dx[0,:] = np.subtract(mB.locations[0,:], mB.locations[0,0])
    dx[1,:] = np.subtract(mB.locations[0,:], mB.locations[0,1])
    tmp = np.multiply((1 - np.divide(l,linit)),dx)
    na_index = np.isnan(tmp)
    tmp[na_index] = 0                       
    F[0,:] = np.sum(-k * tmp , axis = 1)
    a = F / m[0:2]
    v[0,:] = v[0,:] + a[0,:] * dt
    mB.locations = mB.locations + v * dt
    locations.append(mB.locations)
    t += 1
    l = length_calculation(mB)
    if t == 50:
        moving = False






 
