# -*- coding: utf-8 -*-
"""
Created on Mon Oct 9 18:41:00 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.
"""

import solution
import pddl
import random

def search(s0, maxIteration, maxTabuSize):
    """
        Given an initial and valid solution we search an optimal solution of the problems
    """
    sBest = s0
    print("Initial solution has a fitness of : " + str(fitness(sBest)))
    tabuList = []
    tabuList.append(s0)
    bestCandidate = s0
    currentIteration = 0
    while maxIteration > currentIteration:
        sN = neighborhood(bestCandidate)
        if len(sN) == 0:
            print("No neighborhood")
            return sBest

        bestCandidate = sN[0]
        for sCandidate in sN:
            if sCandidate not in tabuList and fitness(sCandidate) < fitness(bestCandidate):
                bestCandidate = sCandidate

        if fitness(bestCandidate) < fitness(sBest):
            sBest = bestCandidate
            print("New solution found with a fitness of : " + str(fitness(sBest)))

        tabuList.append(bestCandidate)

        if len(tabuList) > maxTabuSize:
            tabuList.pop(0)

        print("Iteration " + str(currentIteration))
        currentIteration = currentIteration + 1
    return sBest

def neighborhood(S):
    """
        Given a solution we compute all valid solution which are in the neighborhood
    """
    # multiple stategies :
    #   for each guard changes only one value randomly with another
    #   for guard X and guard Y (choose randomly) changes only one value randomly with another
    solutions = []
    sN = S

    for guard in S.guardsPath:
        x = 0
        y = 0
        while x == y:
            x = random.randint(0, len(guard)-1)
            y = random.randint(0, len(guard)-1)
        mem = guard[x]
        guard[x] = guard[y]
        guard[y] = mem

    if pddl.check(S):
        solutions.append(S)
    return solutions

def fitness(S):
    """
        The fitness function computes the sum of all guard's round 
    """
    sum = 0
    for path in S.guardsPath:
        for i in range(1, len(path)-1):
            completePath = S.map.getPath(int(path[i-1]/S.map.getLength()), int(path[i-1]%S.map.getLength()), int(path[i]/S.map.getLength()), int(path[i]%S.map.getLength()))
            sum += len(completePath)
    return sum