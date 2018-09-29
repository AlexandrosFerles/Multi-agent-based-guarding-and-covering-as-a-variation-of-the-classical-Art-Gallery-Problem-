# -*- coding: utf-8 -*-
"""

Created on Wed Oct 11 09:55:21 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.

"""

from random import randrange
import decimal
import numpy as np
import tabuSearch
import pddl
from copy import deepcopy
import solution
import time

# function that performs the cross-over
# combination of 2 solution lists

def combine(parent1, parent2, min_step, max_step):
    # cut the piece of the first parent
    temp = parent1[min_step: max_step]
    solve = []
    cnt = 0
    i = 0

    while (cnt < min_step):
        # append only elements not
        # in the first parent's slice
        if (parent2[i] not in temp):
            solve.append(parent2[i])
            cnt += 1
        i += 1
    # jointhe slice in the appropriate
    # position of the result
    solve += temp
    # join the rest of the elements
    while (i < len(parent2)):
        if (parent2[i] not in temp):
            solve.append(parent2[i])

    return solve


# solutions list
# flag for merging all possible combinations
def CrossOver(solutions, flag):
    res = []

    step = np.random.normal(0.1, 0.05)

    # set starting and end indexes of the slice
    cut_piece = round(len(solutions[0]) * step)
    min_step = randrange(0, len(solutions[0]) - cut_piece)
    max_step = min_step + cut_piece

    if (flag):

        start =0
        for parent1 in solutions[start:]:
            for parent2 in solutions[start+1:]:
                res.append(combine(parent1, parent2, min_step, max_step))
                start+=1
    else:
        used = []
        if len(solutions) % 2 == 1:
            res = [solutions[0]]
            solutions = solutions[1:]
        while (len(used) < len(solutions)):

            parent1 = []
            parent2 = []

            while (True):
                index_1 = randrange(len(solutions))
                if (index_1 not in used):
                    used.append(index_1)
                    parent1 = solutions[index_1]
                    break

            while (True):
                index_2 = randrange(len(solutions))
                if (index_2 not in used):
                    used.append(index_2)
                    parent2 = solutions[index_2]
                    break

            # we make sure that all elements of the solutions
            # list are used only once for tηe crossovers
            res.append(combine(parent1, parent2, min_step, max_step))

    return res


def mutation(solutions, possibility = 0.1):
    # compute a random possibility in [0,1]

    # if possibility i1s within range
    # randonly mutate two neihgbours
    # of the solution

    for elem in solutions:
        for i in range( len(elem.guardsPath) ):
            allow = float(decimal.Decimal(randrange(0, 100)) / 100)

            if (allow < possibility):
                g=elem.guardsPath[i]
                index = randrange(0, len(g)-1)

                # swap neighbors
                temp = g[index]
                g[index] = g[index + 1]
                g[index + 1] = temp

                elem.guardsPath[i]=g


    return solutions


def get_solutions(m, numberOfGuards, numOfsol):
    solutions = []
    for sol in range(numOfsol):
        solutions .append( pddl.getSolution( m , numberOfGuards ) )
    return solutions

def get_fitness(solutions):
    fit = []
    for s in solutions:
        debug = tabuSearch.fitness(s)
        fit.append(tabuSearch.fitness(s))
        
    return fit
  
def multiCrossOver(solutions, flag,number_of_guards, myMap):

    guard_and_solutions=[]

    for i in range(number_of_guards):

        temp=[]
        for s in solutions:
            temp.append(s.guardsPath[i])

        guard_and_solutions.append(temp)

    check = zip(*guard_and_solutions)
    res=[]
    for elem in check:
        newSol = solution.Solution(_map=myMap, _numberOfGuards=number_of_guards, _guardsPath=list(list(elem)))
        res.append(newSol)

    return res
        

def GA(m, numberOfGuards, file, max_gen = 10):
    start_time = time.time()

    # set maximum generations
    #max_gen = 100
    # set threshold for elitism
    elit_th = 2000
    # set maximum elit parents
    n_best = 5
    # set number of generated solutions
    numOfsol = 10

    # get solutions
    solutions = get_solutions(m, numberOfGuards, numOfsol)
    # get solutions size
    sol_size = len(solutions)
    
    # initialize performance
    performance =[]
    # start generations
    for gen in range(max_gen):
        childs = []
        parents = []
        population = []

        # get fitness
        fit = get_fitness(solutions)

        # get average ftiness
        avgSol = float(sum(fit)) / len(fit)
        # get as candidate parents those who have fitness > average of the generation
        bestIdx = [index for index, value in enumerate(fit) if value < avgSol]
        parents += (list(solutions[i] for i in bestIdx))

        # do cross over
        population += multiCrossOver(parents, False, numberOfGuards,m)

        # make sure that the population's size is constant
        if gen == elit_th + 1:
            sol_size = sol_size - n_best
        if len(population) > sol_size:
            evalPop = get_fitness(population)
            bestPop = sorted(range(len(evalPop)), key=lambda i: evalPop[i])[:evalPop]
            population = list(population[i] for i in bestPop)
        else:
            population += (get_solutions(m, numberOfGuards, abs(len(population) - sol_size)))

        # do cross mutation
        childs += (mutation(population))

        # if generations > 20 do elitism
        if gen > elit_th:
            elit = sorted(range(len(fit)), key=lambda i: fit[i])[:n_best]
            fit += elit
            childs += (list(parents[i] for i in elit))

        solutions = deepcopy(childs)
        
        # get the best solution so far
        fit = get_fitness(solutions)
        bestFit = sorted(range(len(fit)), key=lambda i: fit[i])[:1]
        bestSolution = solutions[bestFit[0]]
        bestFitness = tabuSearch.fitness(bestSolution)
        performance.append(bestFitness)
        
        # print('Iteration '+str(gen) + ' ends with fitness = ' + str(bestFitness) + '\n')
        file.write('Iteration '+str(gen) + ' ends with fitness = ' + str(bestFitness) + '\n')

    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s minutes ---" % (time.time() - start_time)/60.0 )
    print("--- %s hours ---" % (time.time() - start_time)/3600.0 )


    return bestSolution, performance
