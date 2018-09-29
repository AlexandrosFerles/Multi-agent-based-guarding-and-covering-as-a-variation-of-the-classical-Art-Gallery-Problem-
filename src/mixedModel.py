# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:42:25 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.
"""

import tabuSearch
import genetic
import simulatedAnnealing
import pddl

def tabu2genetic(TSnum, _map, _numberOfGuards, _maxTabuMemory, _maxIteration):
    # TSnum is th number of TS solutions that will pass into the GA
    tabuSolutions = []
    
    for i in range(TSnum):
            # initialize a solution
        initialSolution = pddl.getSolution(_map, _numberOfGuards)
        # pass solution in TS and get an optimal TS path
        tabuSolutions.append(tabuSearch.search(initialSolution, _maxIteration, _maxTabuMemory))
    # pass TS solutions to GA
    optSolutions = genetic.GA(tabuSolutions)
    
    return optSolutions

def sa2genetic(SAnum, _t0, _tMin, _eMax):
    # SAnum is th number of TS solutions that will pass into the GA
    SAsolutions = []
    
    for i in range(TSnum):
            # initialize a solution
        initialSolution = pddl.getSolution(_map, _numberOfGuards)
        # pass solution in TS and get an optimal TS path
        SAsolutions.append(simulatedAnnealing.search(_t0, initialSolution, _tMin, _eMax, deltaT = 0.1))
        
    # pass SA solutions to GA
    optSolutions = genetic.GA(SAsolutions)
    
    return optSolutions


"""
def genetic2sa():
    
    initialSolution = pddl.getSolution(_map, _numberOfGuards)
    
    
    return optSolutions
    
def tabu2sa():
    
    initialSolution = pddl.getSolution(_map, _numberOfGuards)
    
    
    return optSolutions
    
def genetic2tabu():
    
    initialSolution = pddl.getSolution(_map, _numberOfGuards)
    
    
    return optSolutions
    
def sa2tabu():
    
    initialSolution = pddl.getSolution(_map, _numberOfGuards)
    
    
    return optSolutions
    """