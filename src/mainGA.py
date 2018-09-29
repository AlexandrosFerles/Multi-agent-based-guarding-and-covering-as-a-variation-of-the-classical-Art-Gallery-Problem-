# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:39:09 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.
"""

testcases=[
'Number_of_guards=5,area_size=900.pkl',
'Number_of_guards=7,area_size=3600.pkl',
'Number_of_guards=1,area_size=3600.pkl',
'Number_of_guards=9,area_size=1600.pkl',
'Number_of_guards=3,area_size=1600.pkl',
'Number_of_guards=7,area_size=2500.pkl',
'Number_of_guards=2,area_size=900.pkl',
'Number_of_guards=8,area_size=4900.pkl',
'Number_of_guards=7,area_size=4900.pkl',
'Number_of_guards=4,area_size=900.pkl',
'Number_of_guards=9,area_size=900.pkl',
'Number_of_guards=9,area_size=400.pkl',
'Number_of_guards=4,area_size=4900.pkl',
'Number_of_guards=8,area_size=6400.pkl',
'Number_of_guards=9,area_size=8100.pkl',
'Number_of_guards=2,area_size=3600.pkl',
'Number_of_guards=6,area_size=400.pkl',
'Number_of_guards=4,area_size=2500.pkl',
'Number_of_guards=4,area_size=6400.pkl',
'Number_of_guards=8,area_size=3600.pkl',
'Number_of_guards=5,area_size=6400.pkl',
'Number_of_guards=1,area_size=4900.pkl',
'Number_of_guards=3,area_size=2500.pkl',
'Number_of_guards=3,area_size=6400.pkl',
'Number_of_guards=3,area_size=400.pkl',
'Number_of_guards=7,area_size=900.pkl',
'Number_of_guards=7,area_size=6400.pkl',
'Number_of_guards=4,area_size=400.pkl',
'Number_of_guards=3,area_size=3600.pkl',
'Number_of_guards=6,area_size=900.pkl',
'Number_of_guards=6,area_size=2500.pkl',
'Number_of_guards=7,area_size=8100.pkl',
'Number_of_guards=1,area_size=400.pkl',
'Number_of_guards=1,area_size=1600.pkl',
'Number_of_guards=4,area_size=1600.pkl',
'Number_of_guards=6,area_size=8100.pkl',
'Number_of_guards=2,area_size=6400.pkl',
'Number_of_guards=4,area_size=8100.pkl',
'Number_of_guards=6,area_size=4900.pkl',
'Number_of_guards=3,area_size=900.pkl',
'Number_of_guards=5,area_size=2500.pkl',
'Number_of_guards=9,area_size=6400.pkl',
'Number_of_guards=5,area_size=8100.pkl',
'Number_of_guards=8,area_size=1600.pkl',
'Number_of_guards=2,area_size=1600.pkl',
'Number_of_guards=2,area_size=400.pkl',
'Number_of_guards=2,area_size=8100.pkl',
'Number_of_guards=8,area_size=2500.pkl',
'Number_of_guards=5,area_size=3600.pkl',
'Number_of_guards=7,area_size=1600.pkl',
'Number_of_guards=2,area_size=4900.pkl',
'Number_of_guards=5,area_size=1600.pkl',
'Number_of_guards=5,area_size=4900.pkl',
'Number_of_guards=9,area_size=2500.pkl',
'Number_of_guards=7,area_size=400.pkl',
'Number_of_guards=6,area_size=6400.pkl',
'Number_of_guards=1,area_size=6400.pkl',
'Number_of_guards=8,area_size=400.pkl',
'Number_of_guards=1,area_size=2500.pkl',
'Number_of_guards=9,area_size=3600.pkl',
'Number_of_guards=5,area_size=400.pkl',
'Number_of_guards=8,area_size=8100.pkl',
'Number_of_guards=6,area_size=3600.pkl',
'Number_of_guards=8,area_size=900.pkl',
'Number_of_guards=3,area_size=8100.pkl',
'Number_of_guards=4,area_size=3600.pkl',
'Number_of_guards=6,area_size=1600.pkl',
'Number_of_guards=9,area_size=4900.pkl',
'Number_of_guards=1,area_size=8100.pkl',
'Number_of_guards=1,area_size=900.pkl',
'Number_of_guards=2,area_size=2500.pkl',
'Number_of_guards=3,area_size=4900.pkl',
]

from model import map
import pddl
import random
from algorithms import tabuSearch
import genetic
import simulatedAnnealing
import matplotlib.pyplot as plt

import pickle

def main():

    # mapSize = 20
    # numberOfGuards = 2
    # numberOfObstacles = 2*numberOfGuards

    # for mapSize in range(20,100,10):
    #     for numberOfGuards in range(1,10):
    # numberOfObstacles = 2*numberOfGuards
    #         m = map.Map(numberOfObstacles, 0, -1, mapSize, mapSize, numberOfGuards)
    #
    #     # for i in range(10):
    #     #     m = map.Map(numberOfObstacles, 0, -1, mapSize, mapSize, numberOfGuards)
    #     #     m.printMap()
    #
    #         with open('Number_of_guards='+str(numberOfGuards)+',area_size='+str(mapSize*mapSize)+'.pkl', 'wb') as output:
    #             pickle.dump(m,output,pickle.HIGHEST_PROTOCOL)


    # with open('map_test0.pkl', 'rb') as input:
    # with open('map_test1.pkl', 'rb') as input:
    # with open('map_test2.pkl', 'rb') as input:
    # with open('map_test3.pkl', 'rb') as input:
    # with open('map_test4.pkl', 'rb') as input:
    # with open('map_test5.pkl', 'rb') as input:
    # with open('map_test6.pkl', 'rb') as input:
    # with open('map_test7.pkl', 'rb') as input:
    # with open('map_test8.pkl', 'rb') as input:
    # with open('map_test9.pkl', 'rb') as input:
    # m=pickle.load(input)
    # m.printMap()

    for testcase in testcases:
        with open(testcase, 'rb') as input:
            m=pickle.load(input)
            m.printMap()

            help=testcase.split('Number_of_guards=')
            numberOfGuards=int(help[1][0])

            initialSolution = pddl.getSolution(m, numberOfGuards)
            print("\nInitial solution\n")
            initialSolution.printMapWithGuardsPath()

            # print("\nFinal solution of Tabu Search\n")
            bestSolution, performance = genetic.GA(m, numberOfGuards)
            bestSolution.printMapWithGuardsPath()
            # plt.plot(performance)
            fig = plt.figure(performance)
            fig.savefig(+str(testcase)+'_performance_plot.png')
    #bestSolution, performance = tabuSearch.search(initialSolution, maxIteration, maxTabuMemory)
    #bestSolution = simulatedAnnealing.search(100, initialSolution, tMin, eMax, deltaT = 0.1)
    # print("\nBegin Genetic Algorithm with memory " + str(maxTabuMemory) + " and for " + str(maxIteration) + " iterations\n")
    #
    # bestSolution = GA(initialSolution,number_of_guards=numberOfGuards)
    #
    # print("\nFinal solution of Genetic Algorithm\n")
    # bestSolution.printMapWithGuardsPath()
    #print("\nBegin TabuSearch with memory " + str(maxTabuMemory) + " and for " + str(maxIteration) + " iterations\n")



if __name__ == "__main__":
    main()
