# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:39:09 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.
"""


from model import map
import pddl
import random
from algorithms import tabuSearch
from algorithms import simulatedAnnealing
import matplotlib.pyplot as plt
import genetic
import pickle


import pickle

def main():

    mapSize = 20
    numberOfObstacles = 20
    numberOfGuards = 5
    maxIteration = 10
    maxTabuMemory = 5

    temperatureInit = 1000
    temperatureMin = 900
    eMin = 400
    
    max_gen = 100

    m = map.Map(numberOfObstacles, 0, -1, mapSize, mapSize, numberOfGuards)
    m.printMap()

    path1 = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/Number_of_guards=1,area_size=400.pkl'
    path2 = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/Number_of_guards=1,area_size=900.pkl'
    path3 = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/Number_of_guards=1,area_size=1600.pkl'
    paths=[path1,path2,path3]
    # path = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/N2'
    # path = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/N3'
    # path = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/N4'
    # path = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/N5'
    # path = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/N6'
    # path = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/N7'
    # path = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/N8'
    # path = '/home/ferles/Desktop/Project and Essay/AI_project/ai17_Group20/src/testcases/N9'


    for path in paths:
        with open(path, 'rb') as input:
            file = open(path + '_output.txt', 'w')

            m = pickle.load(input)
            file.write(m.printMap())
            file.write('\n')

            # numberOfGuards=int((testcases[0].split('Number_of_guards='))[1][0])
            numberOfGuards = 1

            initialSolution = pddl.getSolution(m, numberOfGuards)

            for i in range(0, numberOfGuards):
                file.write("\nInitial solution Guard " + str(i) + "\n")
                # print("\nInitial solution Guard " + str(i) + "\n")

                file.write(initialSolution.printMapWithOneGuardsPath(i))
                file.write('\n')

            file.write("\nBegin TabuSearch with memory " + str(maxTabuMemory) + " and for " + str(
                maxIteration) + " iterations\n")
            # print("\nBegin TabuSearch with memory " + str(maxTabuMemory) + " and for " + str(maxIteration) + " iterations\n")
            bestSolution, performance = tabuSearch.search(initialSolution, maxIteration, maxTabuMemory, file)
            plt.plot(performance)
            plt.xlabel('Iteration')
            plt.ylabel('Fitness')
            # plt.savefig(testcases[0]+'_TS_fitEvol.png', bbox_inches='tight')
            plt.savefig(path+'_TS_fitEvol.png', bbox_inches='tight')
            plt.clf()
            # plt.show()
            file.write("\nFinal solution of Tabu Search\n")
            # print("\nFinal solution of Tabu Search\n")
            for i in range(0, numberOfGuards):
                # print("\nBest solution Guard " + str(i) + "\n")
                file.write("\nBest solution Guard " + str(i) + "\n")

                file.write(bestSolution.printMapWithOneGuardsPath(i))

            file.write("\nFinal solution of Tabu Search\n")
            # print("\nFinal solution of Tabu Search\n")
            file.write(bestSolution.printMapWithGuardsPath())
            # bestSolution.printMapWithGuardsPath()

            file.write("\nEach path of guard\n")
            # print("\nEach path of guad\n")
            for g in bestSolution.guardsPath:
                # print(g)
                file.write(str(g) + "\n")
                file.write(str(g) + "\n")
                file.write(str(g) + "\n")

                # print("\nBegin simulatedAnnealing with initial Energy " + str(temperatureInit) + " and for " + "\n")
            file.write("\nBegin simulatedAnnealing with initial Energy " + str(temperatureInit) + " and for " + "\n")
            bestSolution, performance = simulatedAnnealing.search(temperatureInit, initialSolution, temperatureMin,
                                                                  eMin, file)
            plt.plot(performance)
            plt.xlabel('Iteration')
            plt.ylabel('Energy')
            # plt.savefig(testcases[0]+'_SA_fitEvol.png', bbox_inches='tight')
            plt.savefig(path+'_SA_fitEvol.png', bbox_inches='tight')
            plt.clf()
            # plt.show()

            file.write("\nFinal solution of Simulated Annealing\n")
            print("\nFinal solution of Simulated Annealing\n")
            for i in range(0, numberOfGuards):
                file.write("\nBest solution Guard " + str(i) + "\n")
                # print("\nBest solution Guard " + str(i) + "\n")

                # bestSolution.printMapWithOneGuardsPath(i)
                file.write(bestSolution.printMapWithOneGuardsPath(i))

            # print("\nFinal solution of Simulated Annealing\n")
            file.write("\nFinal solution of Simulated Annealing\n")
            file.write(bestSolution.printMapWithGuardsPath())
            # bestSolution.printMapWithGuardsPath()

            file.write("\nEach path of guard\n")
            # print("\nEach path of guad\n")
            for g in bestSolution.guardsPath:
                # print(g)
                file.write(str(g) + "\n")

            file.write("\nBegin genetic with memory with max generations " + str(max_gen) + "\n")
            # print("\nBegin genetic with memory with max generations " + str(max_gen) + "\n")
            bestSolution, performance = genetic.GA(m, numberOfGuards, file, max_gen)
            plt.plot(performance)
            plt.xlabel('Iteration')
            plt.ylabel('Fitness')
            plt.savefig(path+'_GA_fitEvol.png', bbox_inches='tight')
            plt.clf()
            # plt.savefig(testcases[0]+'_GA_fitEvol.png', bbox_inches='tight')
            # plt.show()
            # print("\nFinal solution of Genetic Algorithm\n")
            file.write("\nFinal solution of Genetic Algorithm\n")
            for i in range(0, numberOfGuards):
                file.write("\nBest solution Guard " + str(i) + "\n")
                # print("\nBest solution Guard " + str(i) + "\n")
                file.write(bestSolution.printMapWithOneGuardsPath(i))
                # bestSolution.printMapWithOneGuardsPath(i)

            file.write("\nFinal solution of Genetic Algorithm\n")
            # print("\nFinal solution of Genetic Algorithm\n")
            file.write(bestSolution.printMapWithGuardsPath())
            # bestSolution.printMapWithGuardsPath()

            file.write("\nEach path of guard\n")
            # print("\nEach path of guard\n")
            for g in bestSolution.guardsPath:
                # print(g)
                file.write(str(g) + "\n")

            file.close()

            print("ALL SET")


    
if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s minutes ---" % (time.time() - start_time)/60.0 )
    print("--- %s hours ---" % (time.time() - start_time)/3600.0 )
