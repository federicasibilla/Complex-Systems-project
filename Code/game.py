# -*- coding: utf-8 -*-

import numpy as np
import random
import math

# Falling ball game

# stage : a grid NxN      (0,0)----->(0,N-1)
#                           |
#                           |
#                           |
#                           ˇ
#                       (N-1,0)

# X balls of 1 pixel will fall one by one from the top of the grid to the 
# bottom. A platform of 3 pixels large is positioned at the bottom line and can
# move left or right. Each ball will be green or red with equal probability.
# The platform has to catch the green balls but not the red ones.

# inputs :  chromosome of length 2*(N-1)*(2*(N-1)+1) : rules to play
#           N : len of side of grid
#           lbd : paramter lambda
#           s : size of pod

# Chromosome structure
# g  g  g  g  .... g  g  g .... r r r r
# y1 y1 y1 y1 .... y2 y2 y2
# x1 x2 x3 x4 .... x1 x2 x3 
# with possible values -1 (move left) or 1 (move 1)
# should work also if we add 0 (stay still)

# output : average fitness of the chromosome after 100 balls

def falling_ball_game(rules, N, lbd, s):
    try:
        if N/2 == int(N/2) or s/2 == int(s/2):
            1/0
    except:
        print('Error : N and s must be odd, not even !')
    else:
        # number of balls
        nb_balls = 100
        # size of chromosome
        n = len(rules)
        g = 0 # will be mean distance from green ball
        r = 0 # same for red
        nb_green = 0
        nb_red = 0
        for b in np.arange(nb_balls):        
            # assign random color
            color = random.choice(['green', 'red'])
            # assign ball random horizontal position at the top
            x = random.choice(np.arange(N))
            y = 0
            # assign initial middle position of platform
            plat = math.floor(N/2)
            
            # play ! iteration on the ball falling down line by line
            while y <= N-1:
                # evaluation of relative positions
                dx = round(plat - x)
                dy = round((N-1) - y)
                if dy == 0:
                    # take distance to the platform and count balls
                    if color == 'green':
                        nb_green += 1
                        g += abs(dx)
                    else:
                        nb_red += 1
                        r += abs(dx)
                    break
                # find index i in chromosome
                if color == 'green':
                    i = 0
                else:
                    i = n/2
                i += (dy-1)*(2*(N-1)+1)
                i += dx + N-1
                # take order from rule
                rule = rules[round(i)]
                # move left ?
                if rule == -1:
                    if plat > s/2:
                        plat -= 1
                # or move right ?
                elif rule == 1:
                    if plat< (N-1)-s/2:
                        plat += 1        
                y+=1
        # normalize distances to number of balls of the right color
        g = g/nb_green
        r = r/nb_red
        # compute fitness with average distances
        f = 1/(1+np.exp(-lbd*((s/2) - g))) - 1/(1+np.exp(-lbd*((s/2) - r))) + 1
        
        # compute fitness' max and min possible value 
        fmax = 1/(1+np.exp(-lbd*(s/2))) - 1/(1+np.exp(-lbd*((s/2) - (N-1)))) + 1
        fmin = 1/(1+np.exp(-lbd*((s/2) - (N-1)))) - 1/(1+np.exp(-lbd*(s/2))) + 1
        # normalize fitness between 1 and 2 in order to compare with paper
        f = 1 + (f-fmin)/(fmax-fmin)
        
        return f

 
# N = 9 # size of grid, must be odd /!\
# s = 3 # length of pod, must be odd /!\
# lbd = 0.5 # paramter lambda

#test_rule = np.zeros(2*(N-1)*(2*(N-1)+1))
#for i in np.arange(len(test_rule)):
#    test_rule[i] = random.choice([-1, 1])

#print(falling_ball_game(test_rule, N, lbd, s))
        