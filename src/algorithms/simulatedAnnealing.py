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
import math

def search(t0, s0, tMin, eMin ,file, deltaT = 0.5):
    """
        This function execute the simulated annealing given an
        initial temperature, an initial solution,
        a minimal temperature,
        a minimal probability and deltaT
    """
    t = t0 # initial temperature
    s = deepcopy(s0) # initial state
    file.write("Initial solution has an energy of : " + str(energy(s))+"\n")
    # print("Initial solution has an energy of : " + str(energy(s)))
    e = energy(s)
    performance =[]
    performance.append(e)
    while t > tMin and e > eMin:
        file.write("Try to find a solution\n")
        # print("Try to find a solution")
        sN = neighborhood(s)
        for sPoss in sN:
            file.write("solution has an energy of : " + str(energy(sPoss))+"\n")
            # print("solution has an energy of : " + str(energy(sPoss)))
            eN = energy(sPoss)
            if eN < e or random.uniform(0, 1) < math.exp(-(e - eN)/t):
                file.write("We take this solution\n")
                # print("We take this solution")
                s = deepcopy(sPoss)
                e = eN
        t = t - deltaT
        performance.append(e)
        
    return s, performance

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
            while x == y and iteration < len(guard) and len(guard) > 2:
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

def energy(S):
    """
        The energy function computes the sum of all guard's round 
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
