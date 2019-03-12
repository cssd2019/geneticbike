#!/usr/bin/env python

from bike import Bike
import numpy as np
import time


# mB is the moving bike 
mB = Bike("random")

# masses of points as activeWheel, passiveWheel, handle1, handle2
m = np.array([0.5, 0.5, 30, 30])

# initial velocities of points
v = np.zeros((2,4))

# spring constant is 5 N/m
# gravity constant is 9.8 m/s**2
k = 5 
g = 9.8
dt = 1


moving = True
while moving == True:

    # F contains forces in x and y-direction
    # spring force will be computed in x direction
    # springForce = k * dl
    # gravity force will be computed in addition to spring force in y direction
    # gravityForce = m * g
    
    F = np.zeros((2,4))
    

    # computation of forces in x-direction
    
    dx = np.zeros((4,4))
    dx[0,:] = np.subtract(mB.locations[0,:], mB.locations[0,0])
    dx[1,:] = np.subtract(mB.locations[0,:], mB.locations[0,1])
    dx[2,:] = np.subtract(mB.locations[0,:], mB.locations[0,2])
    dx[3,:] = np.subtract(mB.locations[0,:], mB.locations[0,3])
                              
    F[0,:] = np.sum(-k * dx, axis = 1)
    

    # computation of forces in y-direction
 
    dy = np.zeros((4,4))
    dy[0,:] = np.subtract(mB.locations[1,:], mB.locations[1,0])
    dy[1,:] = np.subtract(mB.locations[1,:], mB.locations[1,1])
    dy[2,:] = np.subtract(mB.locations[1,:], mB.locations[1,2])
    dy[3,:] = np.subtract(mB.locations[1,:], mB.locations[1,3])
                              
    F[1,:] = np.sum(-k * dy - m * g, axis = 1)
    

    # computation of acceleration
    a = F / m
    

    # computation of velocity
    v = v + a * dt
    print(v)
    time.sleep(3)
    
    # computation of new locations of the points 
    mB.locations = mB.locations + v * dt
    print(mB.locations)
    time.sleep(5.5)
    if mB.locations[1,2] == 0 or mB.locations[1,3] == 0:
        moving = False
