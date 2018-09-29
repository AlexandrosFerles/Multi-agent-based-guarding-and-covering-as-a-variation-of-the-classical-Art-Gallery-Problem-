# -*- coding: utf-8 -*-
"""
Created on Mon Oct 9 18:41:00 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.
"""
import solution
import pddl
import random
from collections import deque
from copy import deepcopy

def search(s0, maxIteration, maxTabuSize,file):
    """
        Given an initial and valid solution we search an optimal solution of the problems
    """
    sBest = deepcopy(s0)
    # print("Initial solution has a fitness of : " + str(fitness(sBest)))
    file.write("Initial solution has a fitness of : " + str(fitness(sBest))+"\n")
    tabuList = deque([s0])
    bestCandidate = deepcopy(sBest)
    currentIteration = 0
    performance =[]
    performance.append(fitness(bestCandidate))
    while maxIteration > currentIteration:
        # print("Best solution has a fitness of : " + str(fitness(sBest)))
        file.write("Best solution has a fitness of : " + str(fitness(sBest))+"\n")
        sN = neighborhood(bestCandidate)
        iteration = 0
        while len(sN) == 0 and iteration < 1000:
            sN = neighborhood(bestCandidate)
            iteration += 1

        if iteration == 1000:
            break
        bestCandidate = deepcopy(sN[0])
        for sCandidate in sN:
            if sCandidate not in tabuList and fitness(sCandidate) < fitness(bestCandidate):
                bestCandidate = sCandidate

        if fitness(bestCandidate) < fitness(sBest):
            sBest = deepcopy(bestCandidate)
            file.write("New solution found with a fitness of : " + str(fitness(sBest))+"\n")
            # print("New solution found with a fitness of : " + str(fitness(sBest)))

        tabuList.append(bestCandidate)

        if len(tabuList) > maxTabuSize:
            tabuList.popleft()

        # print("Iteration " + str(currentIteration))
        file.write("Iteration " + str(currentIteration))
        currentIteration = currentIteration + 1
        performance.append(fitness(sBest))
    file.write("Best solution has a fitness of : " + str(fitness(sBest))+"\n")
    # print("Best solution has a fitness of : " + str(fitness(sBest)))

    return sBest, performance

def neighborhood(S):
    """
        Given a solution we compute all valid solution which are in the neighborhood
    """
    # multiple stategies :
    solutions = []
    sN = deepcopy(S)
    sN1 = deepcopy(S)
    sN2 = deepcopy(S)

    #   Changes only one value randomly with another for each guard
    for guard in sN.guardsPath:
        for i in range(1,20):
            x = 0
            y = 0
            iteration = 0
            while x == y and iteration < len(guard):
                x = random.randint(1, len(guard)-2)
                y = random.randint(1, len(guard)-2)
                iteration += 1
            mem = guard[x]
            guard[x] = guard[y]
            guard[y] = mem

    # Remove some values between guards
    for guard in sN1.guardsPath:
        for i in range(1,min(random.randint(1, 2), len(guard)-2)):
            if i > 0 and i < len(guard)-1:
                guard.pop(i)

    # Change values between guards
    for i in range(1,10):
        g1 = 0
        g2 = 0
        iteration = 0
        while g1 == g2 and iteration < S.numberOfGuards:
            g1 = random.randint(0, S.numberOfGuards-1)
            g2 = random.randint(0, S.numberOfGuards-1)
            iteration += 1

        for j in range(1, 5):
            x = 0
            y = 0
            iteration = 0
            while x == y and iteration < len(guard):
                x = random.randint(1, len(sN2.guardsPath[g1])-2)
                y = random.randint(1, len(sN2.guardsPath[g2])-2)
                iteration += 1

            mem = sN2.guardsPath[g1][x]
            sN2.guardsPath[g1][x] = sN2.guardsPath[g2][y]
            sN2.guardsPath[g2][y] = mem

    if pddl.check(sN):
        solutions.append(sN)

    if pddl.check(sN1):
        solutions.append(sN1)

    if pddl.check(sN2):
        solutions.append(sN2)

    #   for guard X and guard Y (choose randomly) changes only one value randomly with another
    
    return solutions

def fitness(S):
    """
        The fitness function computes the sum of all guard's round 
    """
    sum = 0
    for path in S.guardsPath:
        for i in range(1, len(path)-1):
            completePath = S.map.getPath(int(path[i-1]/S.map.getLength()), int(path[i-1]%S.map.getLength()), int(path[i]/S.map.getLength()), int(path[i]%S.map.getLength()))
            for node in completePath:
                position = node[0]*S.map.getLength()+node[1]
                # Left
                if position-1 >= 0 and position % S.map.getLength() != 1:
                    sum += 1
                # Right
                if position+1 < S.map.getLength() * S.map.getLength() and position % S.map.getLength() != 0:
                    sum += 1

                # Up
                if position-S.map.getLength() >= 0:
                    sum += 1
                # Down
                if position+S.map.getLength() < S.map.getLength() * S.map.getLength():
                    sum += 1

                # Diagonal Up Left
                if position-S.map.getLength()-1 >= 0 and position % S.map.getLength() != 1:
                    sum += 1
                # Diagonal Up Right
                if position-S.map.getLength()+1 >= 0 and position % S.map.getLength() != 0:
                    sum += 1

                # Diagonal Down Left
                if position+S.map.getLength()-1 < S.map.getLength() * S.map.getLength() and position % S.map.getLength() != 1:
                    sum += 1
                # Diagonal Down Right
                if position+S.map.getLength()+1 < S.map.getLength() * S.map.getLength() and position % S.map.getLength() != 0:
                    sum += 1

    return sum
