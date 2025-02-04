#!/usr/bin/env python

from bike import Bike
import numpy as np
import time
import sys
np.seterr(divide='ignore', invalid='ignore')

def length_calculation(mB):
    l = np.zeros((4,4))
    l[0,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,0])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,0])))
    l[1,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,1])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,1])))
    l[2,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,2])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,2])))
    l[3,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,3])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,3])))
    return l

def drop_and_move(floor, mB):
    # spring constant is 5 N/m
    # gravity constant is 9.8 m/s**2
    # time steps are 1s
    # acceleration of active wheel is 4 m/s**2
    k = 5 
    g = 9.8
    dt = 0.1
    a_Aw = 0.4

    locations = list()

    # mB is the moving bike 
    mB.locations[1,:] += 1

    # masses of points as activeWheel, passiveWheel, handle1, handle2 in kg
    m = np.array([0.5, 0.5, 30, 30])

    v = np.zeros((2, 4))

    # is one of two points near the floor is active wheel or is one of the handles touching the floor
    sorted_ind = np.argsort(mB.locations[1,:])
    sorted_y = np.sort(mB.locations[1,:])
    if (sorted_y[0] == mB.locations[1,2]) or (sorted_y[1] == mB.locations[1,2]) or (sorted_y[0] == mB.locations[1,3]) or (sorted_y[1] == mB.locations[1,3]):
        # one of the handle touches the ground
        locations.append(mB.locations)
    if (sorted_y[0] == mB.locations[1,0]) or (sorted_y[1] == mB.locations[1,0]):
        # active wheel touches the ground
        print("enjoy the ride!")
    else:
        # active wheel does not touch the ground
        locations.append(mB.locations)

    inair_firstPoint = True
    inair_secondPoint = True
    t = 0
    locations.append(mB.locations)

    # gravity applies to the bike

    # touch point for point 1
    indexFloor = floor[0,:] == np.floor(mB.locations[0,sorted_ind[0]])
    indexCeil = floor[0,:] == np.ceil(mB.locations[0,sorted_ind[0]])
    indexEq = floor[0,:] == mB.locations[0,sorted_ind[0]]
    if np.any(indexEq):
        y_touch_1 = floor[1,indexEq]
    else:
        y_touch_1 = (floor[1,indexFloor] + floor[1,indexCeil]) / 2

    # touch point for point 2
    indexFloor = floor[0,:] == np.floor(mB.locations[0,sorted_ind[1]])
    indexCeil = floor[0,:] == np.ceil(mB.locations[0,sorted_ind[1]])
    indexEq = floor[0,:] == mB.locations[0,sorted_ind[1]]
    if np.any(indexEq):
        y_touch_2 = floor[1,indexEq]
    else:
        y_touch_2 = (floor[1,indexFloor] + floor[1,indexCeil]) / 2
            
    v[1,:] = - g * dt

    while inair_firstPoint == True or inair_secondPoint == True:
        mB.locations = mB.locations + v * dt
        if y_touch_1 + 0.001 > mB.locations[1,sorted_ind[0]] and y_touch_1 - 0.001 < mB.locations[1,sorted_ind[0]] and inair_firstPoint == True:
            moving = True
            inair_firstPoint = False
            v[1,sorted_ind[0]] = 0
        if y_touch_1 - 0.001 > mB.locations[1,sorted_ind[0]]:
            moving = True
            inair_firstPoint = False
            v[1,sorted_ind[0]] = 0

        if y_touch_2 + 0.001 > mB.locations[1,sorted_ind[1]] and y_touch_2 - 0.001 < mB.locations[1,sorted_ind[1]] and inair_secondPoint == True:
            moving = True
            inair_secondPoint = False
            v[1,sorted_ind[1]] = 0
        if y_touch_2 - 0.001 > mB.locations[1,sorted_ind[1]]:
            moving = True
            inair_secondPoint = False
            v[1,sorted_ind[1]] = 0
        t += 1
        locations.append(mB.locations)

    # the initial length of springs are set here
    linit = length_calculation(mB)

    l = linit

    v[0,:] = a_Aw * dt

    # movement starts
    F = np.zeros((2,4))
    while moving == True:
        dx = np.zeros((4,4))
        dx[0,:] = np.subtract(mB.locations[0,:], mB.locations[0,0])
        dx[1,:] = np.subtract(mB.locations[0,:], mB.locations[0,1])
        dx[2,:] = np.subtract(mB.locations[0,:], mB.locations[0,2])
        dx[3,:] = np.subtract(mB.locations[0,:], mB.locations[0,3])
        tmp = np.multiply((1 - np.divide(l,linit)),dx)
        na_index = np.isnan(tmp)
        tmp[na_index] = 0                       
        F[0,:] = np.sum(-k * tmp , axis = 1)
        dy = np.zeros((4,4))
        dy[0,:] = np.subtract(mB.locations[1,:], mB.locations[1,0])
        dy[1,:] = np.subtract(mB.locations[1,:], mB.locations[1,1])
        dy[2,:] = np.subtract(mB.locations[1,:], mB.locations[1,2])
        dy[3,:] = np.subtract(mB.locations[1,:], mB.locations[1,3])
        tmp = np.multiply((1 - np.divide(l,linit)),dy)
        na_index = np.isnan(tmp)
        tmp[na_index] = 0                       
        F[1,:] = np.sum(-k * tmp + m * g , axis = 1)
        a = F / m
        v[0,:] = v[0,:] + a[0,:] * dt
        v[1,:] = 0
        mB.locations = mB.locations + v * dt
        locations.append(mB.locations)
        t += 1
        l = length_calculation(mB)
        if t == 50:
            moving = False
    print(locations)
    return locations



def test_first():
    floor = np.random.rand(2,10)
    floor[0,:] = np.array([0,1,2,3,4,5,6,7,8,9])
    mB = Bike("random")
    drop_and_move(floor, mB)

test_first()
