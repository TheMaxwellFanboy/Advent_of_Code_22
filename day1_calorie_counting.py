# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:48:43 2022

@author: nkp812
"""

#%% Libraries
import numpy as np



#%%  Puzzle input
raw = list(open('PU_d1_calorie_counting.txt','r'))

#%% Formatting
cal_list = ['_' if x == '\n' else x.replace('\n',',') for x in raw]
cal_stat_list = ''.join(cal_list).split('_')
cal_stat_list = [np.array([int(y) for y in x.split(',')[:-1]]) for x in cal_stat_list]

#%% Answer 1
max_calories = max([sum(x) for x in cal_stat_list])

#%% Answer 2
cals_per_elf = [sum(x) for x in cal_stat_list]
total_top_three = sum(np.sort(cals_per_elf)[-3:])

