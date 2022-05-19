# -*- coding: utf-8 -*-

from GA import GA_falling_ball
import matplotlib.pyplot as plt
import matplotlib.colors as mlpc
import numpy as np
import random as rn
import time
from progress import progress

plt.rc('font', size=18)          # controls default text sizes
plt.rc('axes', titlesize=18)     # fontsize of the axes title
plt.rc('axes', labelsize=18)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
plt.rc('legend', fontsize=16)    # legend fontsize
plt.rc('figure', titlesize=18)  # fontsize of the figure title


###############################################################################
################## HEATMAP FOR FITNESS OVER A`LAMBDA ##########################
###############################################################################

# Fixing variables
N = 15 # size of grid
n=2*(N-1)*(2*(N-1)+1) # length of chromosome
s = 3 # size of pod
lambdas = np.logspace(np.log10(0.05), np.log10(5), 10) # parameter lambda
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
plt.hist2d(X, Y, bins=(lambdas, np.linspace(min(Y),max(Y),20)))
plt.xlabel('$\\lambda$')
plt.ylabel('fitness')
plt.xscale('log')
plt.xlim([lambdas[0], lambdas[-1]])
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