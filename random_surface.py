#!/usr/bin/python

import numpy as np
from random import random


def create_random_surface(n=100):
    vals = [random() * (22/7) for _ in range(2*n)]
    avg = [np.sin(x) for x in vals]
    avg = np.convolve(avg, np.ones((n,))/n, mode='valid')
    
    avg = list(avg)
    avg = [str(x) for x in avg]
    with open('./random_surface.csv', 'w') as f:
        f.write(','.join(avg))


def read_np_random_surface(filename):
    with open(filename, 'r') as f:
        pts = f.read()
    pts = pts.split(',')
    xs = range(101)
    pts = [float(x) for x in pts]
    pts = np.concatenate((xs, pts))
    pts = pts.reshape((2, 101))
    
    return pts
