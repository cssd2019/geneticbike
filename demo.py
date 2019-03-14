#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[18]:


import numpy as np
from bike import Bike
import visuals
from bike_moving_w_constant_velocity import drop_and_move
from random_surface import read_np_random_surface


# In[19]:


#floor = np.random.rand(2,10)
#floor[0,:] = np.array([0,1,2,3,4,5,6,7,8,9])
floor = read_np_random_surface('random_surface.csv')
bike=Bike(np.array([[0,1,0,1],[0,0,1,1]]))
locs = drop_and_move(floor, bike)

locs = locs[::2]

# In[20]:


type(locs)


# In[ ]:


visuals.animate(floor, locs)
