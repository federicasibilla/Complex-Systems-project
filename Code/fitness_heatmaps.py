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

N = 15
n=2*(N-1)*(2*(N-1)+1)
s = 3
lambdas = np.logspace(0.05, 5, 10)
X = [] # lambdas for heatmap
Y = [] # fitnesses for heatmap

samples = 20 # nb of fitnesses computed per lambda
generations = 100 # nb of generation of GA

tic = time.perf_counter()
for i,l in enumerate(lambdas):
    for m in range(samples):
        frac = i/len(lambdas) + m/(len(lambdas)*samples)
        progress(frac, tic)
        # compute initial population
        trial_chromosomes=array = np.ones((51,n))
        for row in range(trial_chromosomes.shape[0]):
            for column in range(trial_chromosomes.shape[1]):
                if rn.random()<0.5: trial_chromosomes[row][column]-=2
        
        X = np.append(X, l)
        Y = np.append(Y, GA_falling_ball(trial_chromosomes, generations, N, l, s)[0])
        
plt.figure()
plt.hist2d(X, Y)
plt.xlabel('$\\lambda$')
plt.ylabel('fitness')
plt.xscale('log')
plt.colorbar()
plt.tight_layout()
plt.show()