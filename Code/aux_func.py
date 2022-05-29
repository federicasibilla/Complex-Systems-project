from game import falling_ball_game

import numpy as np
import random as rn
from copy import copy, deepcopy

# ------------------ Auxiliary functions -------------------------------------------------------------------------
# ------------------ Parents selection function ------------------------------------------------------------------
# INPUTS:  method: string referring to what method we want to use to select the parents
#                  options are: 'ranking_proportional','fitness_proportional'
#          population: matrix of chromosomes among which to choose parents
#          n: integer number of chromosomes to use as parents
#          N, lbd, S: see below
# RETURNS: array of indices of the selected parents in the population matrix

def parent_selection(method, population, n, N, lbd, s):

    current_population_fitness=[falling_ball_game(chromosome, N, lbd, s) for chromosome in population]

    # first method: probability of being selected is proportional to ranking fitness position
    if method=='ranking_proportional':
        
        # rank and select parents (n: 1 is the best performing, the others selected with p proportional to ranking position)
        sorted_indices=list(np.argsort(current_population_fitness))
        weights = np.asarray([(l+1) for l in range(len(current_population_fitness)-1)])
        parents_indices = np.append(sorted_indices[-1],np.random.choice(sorted_indices[1:], size=n-1, replace=False, p=weights/sum(weights)))
    
    # choose fitness proportional selection: probability is proportional to fitness
    if method=='fitness_proportional':
        
        # choose 25 chromosomes  
        sorted_indices=np.argsort(current_population_fitness)[::-1] 
        cpf=np.argsort(current_population_fitness)[::-1][1:n+1]
        
        parents_indices = np.append(sorted_indices[0],np.random.choice(sorted_indices[1:n+1], size=n-1, replace=False, p=cpf/sum(cpf)))


    return parents_indices

# ------------------ Generation of offspring method --------------------------------------------------------------
# INPUTS:  parents_indices: array of indices from current generation of selected parents
#          current_population: matrix with chromosomes from current population
#          method: string with name of method used to generate offspring
#                  'two_by_two': for every couple of 2 kids chromosomes we have a chosen probability of cross-over, otherwise parents are just copied
#                  'traditional_cross': same as 2 by 2 but croos over is performed traditionally
#                  'probability_reproduction': we choose a new couple until reproduction can happen
# RETURNS: matrix with new generation

def offspring_method(parents_indices, current_population, method):

    # choose method 'two_by_two', generations all have the same size as initial population, which has to be odd
    if method=='two_by_two':

        if current_population.shape[0] % 2 == 0: 
            print('population size must be odd for this method!')
            return

        # inizialize empty matrix to store offspring 
        new_generation=np.zeros(current_population.shape) 

        # perform elitism by assigning last chromosome to the best performing in past generation
        new_generation[-1]=current_population[parents_indices[0]]

        # loop over all empty chromosomes 2 by 2 and cross-over with probability 0.25 
        for j in  range(0,new_generation.shape[0]-1,2):

            # choose parents amond possible parents and crossing point completely random
            cross_point = rn.randint(0,len(new_generation[j]))
            from_cr=len(new_generation[j])-cross_point
            parents = rn.sample(list(parents_indices), k=2)

            # with probability 0.25 perform crossover
            cross_p=rn.random()
            
            if cross_p<0.25:
                new_generation[j][cross_point:]=current_population[parents[0]][cross_point:]
                new_generation[j][:cross_point]=current_population[parents[1]][from_cr:]
                new_generation[j+1][:from_cr]=current_population[parents[1]][:from_cr]
                new_generation[j+1][from_cr:]=current_population[parents[0]][:cross_point]
            else:
                new_generation[j][:]=current_population[parents[0]][:]
                new_generation[j+1][:]=current_population[parents[1]][:]
        
        # random mutation with probability 0.01 per locus
        for chromosome in new_generation:
            for gene in chromosome:
                if rn.random()<0.01:
                    if gene==1: gene=gene-2
                    elif gene==-1: gene=gene+2

    # choose method 'traditional_Cross', generations all have the same size as initial population, which has to be odd
    if method=='traditional_cross':

        if current_population.shape[0] % 2 == 0: 
            print('population size must be odd for this method!')
            return

        # inizialize empty matrix to store offspring 
        new_generation=np.zeros(current_population.shape) 

        # perform elitism by assigning last chromosome to the best performing in past generation
        new_generation[-1]=current_population[parents_indices[0]]

        # loop over all empty chromosomes 2 by 2 and cross-over with probability 0.25 
        for j in  range(0,new_generation.shape[0]-1,2):

            # choose parents amond possible parents and crossing point completely random
            cross_point = rn.randint(0,len(new_generation[j]))
            parents = rn.sample(list(parents_indices), k=2)

            # with probability 0.25 perform crossover
            cross_p=rn.random()
            
            if cross_p<0.25:
                new_generation[j][cross_point:]=current_population[parents[0]][cross_point:]
                new_generation[j][:cross_point]=current_population[parents[1]][:cross_point]
                new_generation[j+1][:cross_point]=current_population[parents[1]][:cross_point]
                new_generation[j+1][cross_point:]=current_population[parents[0]][cross_point:]
            else:
                new_generation[j][:]=current_population[parents[0]][:]
                new_generation[j+1][:]=current_population[parents[1]][:]
        
        # random mutation with probability 0.01 per locus
        for chromosome in new_generation:
            for gene in chromosome:
                if rn.random()<0.01:
                    if gene==1: gene=gene-2
                    elif gene==-1: gene=gene+2
    
    # choose method 'probability_reproduction', generations all have the same size as initial population, which has to be odd
    if method=='probability_reproduction':
        if current_population.shape[0] % 2 == 0: 
            print('population size must be odd for this method!')
            return
        # inizialize empty matrix to store offspring 
        new_generation=np.zeros(current_population.shape) 

        # perform elitism by assigning last chromosome to the best performing in past generation
        new_generation[-1]=current_population[parents_indices[0]]

        for j in  range(0,new_generation.shape[0]-1,2):
            # choose parents amond possible parents and crossing point completely random
            cross_point = rn.randint(0,len(new_generation[j]))
            
            # choose two parents until probability of mating is satisfied
            cross_p=rn.random()
            if cross_p<0.25:
                # choose parents amond possible parents and crossing point completely random
                cross_point = rn.randint(0,len(new_generation[j]))
                parents = rn.sample(list(parents_indices), k=2)
            else:
                while(cross_p>0.25):
                    parents = rn.sample(list(parents_indices), k=2)
                    cross_p=rn.random()
            
            new_generation[j][cross_point:]=current_population[parents[0]][cross_point:]
            new_generation[j][:cross_point]=current_population[parents[1]][:cross_point]
            new_generation[j+1][:cross_point]=current_population[parents[1]][:cross_point]
            new_generation[j+1][cross_point:]=current_population[parents[0]][cross_point:]
            
        # random mutation with probability 0.01 per locus
        for chromosome in new_generation:
            for gene in chromosome:
                if rn.random()<0.01:
                    if gene==1: gene=gene-2
                    elif gene==-1: gene=gene+2
    
    return new_generation
