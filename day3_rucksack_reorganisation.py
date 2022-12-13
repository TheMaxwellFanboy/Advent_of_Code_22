# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:48:43 2022

@author: nkp812
"""

#%% Libraries
import numpy as np



#%%  Puzzle input
raw = list(open('PU_d3_rucksack_reorganisation.txt','r'))
#%% Formatting
inventory = [x.replace('\n','') for x in raw]

inv_splitted = [[x[:int(len(x)/2)],x[int(len(x)/2):]] for x in inventory]

#%% Find errors 
error_list = [[]] * len(inventory)
for idx,(x,y) in enumerate(inv_splitted):
    for item in x:
        if item in y:
            error_list[idx] = item
            
#%% Calculate priorites
# Solve for difference between ord(letter) and advent scoring (as), i.e. ord('z') - as('z') = 96
lower_offset = ord('z')-26
upper_offset = ord('Z')-52

def priority_calc(item):
    if item == item.upper():
        priority = ord(item)-upper_offset
    else:
        priority = ord(item)-lower_offset
    return priority

#%% Calculating Answer 1
sum_of_priorities = sum([priority_calc(x) for x in error_list])



#%% Answer 2 - Badges





        