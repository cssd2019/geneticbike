#!/usr/bin/env python

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


def read_floor(floor_file):
    with open(floor_file, 'r') as f:
        floor = f.read()
    floor = floor.split(',')
    floor = [float(x) for x in floor]
    
    return floor