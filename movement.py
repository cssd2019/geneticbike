#!/usr/bin/env python

from bike import Bike
import numpy as np
import time
np.seterr(divide='ignore', invalid='ignore')

def length_calculation(mB):
    l = np.zeros((4,4))
    l[0,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,0])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,0])))
    l[1,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,1])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,1])))
    l[2,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,2])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,2])))
    l[3,:] = np.sqrt(np.square(np.subtract(mB.locations[0,:], mB.locations[0,3])) + np.square(np.subtract(mB.locations[1,:], mB.locations[1,3])))
    return l
# mB is the moving bike 
mB = Bike("random")

# masses of points as activeWheel, passiveWheel, handle1, handle2 in kg
m = np.array([0.5, 0.5, 30, 30])

# initial velocities of points - that could be calculated initially ??
v = np.random.rand(2, 4)

# spring constant is 5 N/m
# gravity constant is 9.8 m/s**2
# time steps are 1s
k = 5 
g = 9.8
dt = 1

# the initial length of springs are set here
linit = length_calculation(mB)

l = linit
moving = True
F = np.zeros((2,4))

while moving == True:

    # F contains forces in x and y-direction
    # spring force will be computed in x direction
    # springForce = k * dl
    # gravity force will be computed in addition to spring force in y direction
    # gravityForce = m * g
    
    # computation of forces in x-direction
    
    dx = np.zeros((4,4))
    dx[0,:] = np.subtract(mB.locations[0,:], mB.locations[0,0])
    dx[1,:] = np.subtract(mB.locations[0,:], mB.locations[0,1])
    dx[2,:] = np.subtract(mB.locations[0,:], mB.locations[0,2])
    dx[3,:] = np.subtract(mB.locations[0,:], mB.locations[0,3])

    tmp = np.multiply((1 - np.divide(l,linit)),dx)
    na_index = np.isnan(tmp)
    tmp[na_index] = 0                       
    F[0,:] = np.sum(-k * tmp , axis = 1)
    print(F)
    time.sleep(5)

    # computation of forces in y-direction
 
    dy = np.zeros((4,4))
    dy[0,:] = np.subtract(mB.locations[1,:], mB.locations[1,0])
    dy[1,:] = np.subtract(mB.locations[1,:], mB.locations[1,1])
    dy[2,:] = np.subtract(mB.locations[1,:], mB.locations[1,2])
    dy[3,:] = np.subtract(mB.locations[1,:], mB.locations[1,3])

    tmp = np.multiply((1 - np.divide(l,linit)),dy)
    na_index = np.isnan(tmp)
    tmp[na_index] = 0      
    F[1,:] = np.sum(-k * tmp - m * g, axis = 1)

    # computation of acceleration
    a = F / m
    

    # computation of velocity
    v = v + a * dt
    
    # computation of new locations of the points 
    mB.locations = mB.locations + v * dt
    l = length_calculation(mB)

    Ymin = min(mB.locations[1,:])
    if Ymin < 0:
        mB.locations[1,:] = np.subtract(mB.locations[1,:], Ymin)
    if mB.locations[1,2] == 0 or mB.locations[1,3] == 0:
        moving = False


