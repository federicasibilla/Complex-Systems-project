# -*- coding: utf-8 -*-

from GA import GA_falling_ball
import matplotlib.pyplot as plt
import numpy as np
import random as rn
import time

plt.rc('font', size=18)          # controls default text sizes
plt.rc('axes', titlesize=18)     # fontsize of the axes title
plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
plt.rc('legend', fontsize=16)    # legend fontsize
plt.rc('figure', titlesize=18)  # fontsize of the figure title


def progress(frac, tic=-1):
    # fancy function to follow progression. to disable it, comment
    # lines 55, 58, 59
    if tic == -1:
        # just some fancy things to follow progression
        print("\033[2K" + str(round(100*frac, 1)) + "%" + '[' +
              round(20*frac)*'='+(20-round(20*frac))*' ' +']', end='\r')
    else:
        # just some fancy things to follow progression
        toc = time.perf_counter()
        mi = str(int((toc-tic)/60))
        sec = str(int((toc-tic) - 60*int(mi)))
        if frac == 0:
            left = 1000
        else:
            left = round((toc-tic)/frac - (toc-tic))
        mi_left = str(int((left/60)))
        sec_left = str(int(left - 60*int(mi_left)))
        if len(sec) == 1:
            sec = '0' + sec
        if len(sec_left) == 1:
            sec_left = '0' + sec_left
        print("\033[2K" + str(round(100*frac, 1)) + "%" + '[' +
              round(20*frac)*'='+(20-round(20*frac))*' ' +']' +
              ' ' + mi + ':' + sec + ' Time left : ' + mi_left + ':'+sec_left + ' ', end='\r')

###############################################################################
################## HEATMAP FOR FITNESS OVER A`LAMBDA ##########################
###############################################################################

# Fixing variables
N = 15 # size of grid
n=2*(N-1)*(2*(N-1)+1) # length of chromosome
s = 3 # size of pod
lambdas = np.logspace(0.05, 5, 10) # parameter lambda
X = [] # lambdas for heatmap
Y = [] # fitnesses for heatmap

samples = 20 # nb of fitnesses computed per lambda
generations = 100 # nb of generation of GA

tic = time.perf_counter() # take time reference
for i,l in enumerate(lambdas): # iterate on lambdas
    for m in range(samples): # take some samples
        frac = i/len(lambdas) + m/(len(lambdas)*samples) # follow progression
        progress(frac, tic) # follow progression
        
        # compute initial population
        trial_chromosomes=array = np.ones((51,n))
        for row in range(trial_chromosomes.shape[0]):
            for column in range(trial_chromosomes.shape[1]):
                if rn.random()<0.5: trial_chromosomes[row][column]-=2
        
        # gather data for heatmap
        X = np.append(X, l)
        Y = np.append(Y, GA_falling_ball(trial_chromosomes, generations, N, l, s)[0])
        
# Plot heatmap

plt.figure()
plt.hist2d(X, Y)
plt.xlabel('$\\lambda$')
plt.ylabel('fitness')
plt.xscale('log')
plt.colorbar()
plt.tight_layout()
plt.show()

###############################################################################
######################## SAME FOR CHANGING s ##################################
######################## COMMENT OTHER LINES ##################################
###############################################################################

# # Fixing variables
# N = 15 # size of grid
# n=2*(N-1)*(2*(N-1)+1) # length of chromosome
# s = [1, 3, 5, 7, 9, 11] # size of pod
# lbd = 0.5 # parameter lambda
# X = [] # s for heatmap
# Y = [] # fitnesses for heatmap

# samples = 20 # nb of fitnesses computed per s
# generations = 100 # nb of generation of GA

# tic = time.perf_counter() # take time reference
# for i,e in enumerate(s): # iterate on s
#     for m in range(samples): # take some samples
#         frac = i/len(s) + m/(len(s)*samples) # follow progression
#         progress(frac, tic) # follow progression
        
#         # compute initial population
#         trial_chromosomes=array = np.ones((51,n))
#         for row in range(trial_chromosomes.shape[0]):
#             for column in range(trial_chromosomes.shape[1]):
#                 if rn.random()<0.5: trial_chromosomes[row][column]-=2
        
#         # gather data for heatmap
#         X = np.append(X, e)
#         Y = np.append(Y, GA_falling_ball(trial_chromosomes, generations, N, lbd, e)[0])
        
# # Plot heatmap
# plt.figure()
# plt.hist2d(X, Y)
# plt.xlabel('$s$')
# plt.ylabel('fitness')
# plt.colorbar()
# plt.tight_layout()
# plt.show()