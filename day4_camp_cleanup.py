# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:48:43 2022

@author: nkp812
"""

#%% Libraries
import numpy as np

#%%  Puzzle input
raw = list(open('PU_d4_camp_cleanup.txt','r'))

#%% Formatting
plot_pairs = [x.replace('\n','').split(',') for x in raw]
plot_max_mins = [x.replace('\n','').replace(',','-').split('-') for x in raw]
plot_max_mins = [[int(y) for y in x] for x in plot_max_mins]

#%% Answer 1 - Full overlap
mask1 = [(x[0]<=x[2]) & (x[1]>=x[3]) for x in plot_max_mins]
mask2 = [(x[2]<=x[0]) & (x[3]>=x[1])  for x in plot_max_mins]
total_overlaps = sum([(x | y) for x,y in zip(mask1,mask2)])


#%% Answer 2 - Any overlap
mask1 = [(x[2]<=x[1]) & (x[3]>=x[0]) for x in plot_max_mins]
# mask2 = [(x[2]<=x[0]) & (x[3]>=x[1])  for x in plot_max_mins]
any_overlaps = sum(mask1)

