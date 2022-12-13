# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:48:43 2022

@author: nkp812
"""

#%% Libraries
import numpy as np



#%%  Puzzle input
raw = list(open('PU_d2_rock_paper_scissors.txt','r'))

#%% Formatting
strat_list = [x.replace('\n','') for x in raw]

#%% Answer 1
def score_calc(round_str):
    outcome = 0
    match round_str.split():
        case [opp,'X']:
            shapepoint = 1
            match opp:
                case 'A':
                    outcome = 3
                case 'C':
                    outcome = 6
        case [opp,'Y']:
            shapepoint = 2
            match opp:
                case 'B':
                    outcome = 3
                case 'A':
                    outcome = 6             
        case [opp,'Z']:
            shapepoint = 3
            match opp:
                case 'C':
                    outcome = 3
                case 'B':
                    outcome = 6 
    total_score = shapepoint + outcome
    return total_score

# calc score
strat_score = sum([score_calc(x) for x in strat_list])

#%% Answer 2
loss_dict = {'A': 'Z',
             'B': 'X',
             'C': 'Y',
             }
draw_dict = {'A': 'X',
             'B': 'Y',
             'C': 'Z',
             }
win_dict = {'A': 'Y',
            'B': 'Z',
            'C': 'X',
            }

def strategy_convert(round_str):
    match round_str.split():
        case [opp,'X']:
            chosen_strat = opp + ' ' + loss_dict[opp]
        case [opp,'Y']:
            chosen_strat = opp + ' ' + draw_dict[opp]
        case [opp,'Z']:
            chosen_strat = opp + ' ' + win_dict[opp]
    return chosen_strat

               
# calc score
new_strat_list = [strategy_convert(x) for x in strat_list]
new_strat_score = sum([score_calc(x) for x in new_strat_list])
