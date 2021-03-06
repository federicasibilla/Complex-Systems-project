from GA import GA_falling_ball
import matplotlib.pyplot as plt
import matplotlib.colors as mlpc
from progress import progress
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

###############################################################################
################## HEATMAP FOR VELOCITY OVER A`LAMBDA #########################
###############################################################################

## Fixing variables
#N = 15 # size of grid
#n=2*(N-1)*(2*(N-1)+1) # length of chromosome
#s = 3 # size of pod
#lambdas = np.logspace(np.log10(0.05), np.log10(5), 10)
#X = [] # lambdas for heatmap
#Y = [] # velocities for heatmap
#
samples = 20 # nb of fitnesses computed per lambda
#desired_fitness = 1.75 # minimum average fitness to reach 
#
tic = time.perf_counter() # take time reference
#
#for i,l in enumerate(lambdas): # iterate on lambdas
#
#    for m in range(samples): # take some samples
#
#        frac = i/len(lambdas) + m/(len(lambdas)*samples) # follow progression
#        progress(frac, tic) # follow progression
#        
#        # compute initial population
#        trial_chromosomes=array = np.ones((51,n))
#        for row in range(trial_chromosomes.shape[0]):
#            for column in range(trial_chromosomes.shape[1]):
#                if rn.random()<0.5: trial_chromosomes[row][column]-=2
#        
#        generations_required=0
#        avg_fitness=0
#        while(avg_fitness<desired_fitness):
#            if generations_required==100:
#               break
#            avg_fitness, new_chromosomes=GA_falling_ball(trial_chromosomes, 1, N, l, s)[0:3:2]
#            trial_chromosomes=new_chromosomes
#            generations_required+=1
#        
#        # gather data for heatmap
#        X = np.append(X, l)
#        Y = np.append(Y, generations_required)
#        
## Plot heatmap
#
#plt.figure()
#plt.hist2d(X, Y, bins=(lambdas, np.linspace(min(Y),max(Y),10)))
#plt.xlim([lambdas[0], lambdas[-1]])
#plt.xscale('log')
#plt.xlabel('$\\lambda$')
#plt.ylabel(f'gen. needed to get to {desired_fitness} fitness')
#plt.colorbar()
#plt.tight_layout()
#plt.show()

###############################################################################
######################## SAME FOR CHANGING s ##################################
######################## COMMENT OTHER LINES ##################################
###############################################################################

# Fixing variables
N = 15 # size of grid
n=2*(N-1)*(2*(N-1)+1) # length of chromosome
s = [1, 3, 5, 7, 9, 11] # size of pod
lbd = 0.5 # parameter lambda
X = [] # s for heatmap
Y = [] # fitnesses for heatmapsamples = 20 # nb of fitnesses computed per lambda
desired_fitness = 1.75 # minimum average fitness to reach tic = time.perf_counter() # take time reference
for i,e in enumerate(s): # iterate on s
    for m in range(samples): # take some samples
        frac = i/len(s) + m/(len(s)*samples) # follow progression
        progress(frac, tic) # follow progression
      
        # compute initial population
        trial_chromosomes=array = np.ones((51,n))
        for row in range(trial_chromosomes.shape[0]):
            for column in range(trial_chromosomes.shape[1]):
                if rn.random()<0.5: trial_chromosomes[row][column]-=2
        generations_required=0
        avg_fitness=0
        while(avg_fitness<desired_fitness):
            if generations_required==100:
                break
            avg_fitness, new_chromosomes=GA_falling_ball(trial_chromosomes, 1, N, lbd, e)[0:3:2]
            trial_chromosomes=new_chromosomes
            generations_required+=1
      
        # gather data for heatmap
        X = np.append(X, e)
        Y = np.append(Y, generations_required)
      
# Plot heatmap
plt.figure()
plt.hist2d(X, Y, bins=(np.linspace(0, 12, 7), np.linspace(min(Y),max(Y),10)))
plt.xlabel('$s$')
plt.xticks(s)
plt.ylabel(f'L( {desired_fitness})')
plt.colorbar()
plt.tight_layout()
plt.show()
