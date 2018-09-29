# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:00:00 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.
"""

from model import map
from copy import deepcopy

class Solution:
    """
        This class represents a state (a possible or not solution)
        A solution is composed of :
            schedule:   The schedule give us for each node and for each turn who visited the node
                        For each point we have a set of NodeSchedule
            numberOfGuards : Number of guards in the state
    """
    __slot__ = ["map", "guardsPath", "numberOfGuards"]

    def __init__(self, _map, _numberOfGuards, _guardsPath):
        self.map = _map
        self.numberOfGuards = _numberOfGuards
        self.guardsPath = _guardsPath

    def printMapWithGuardsPath(self):
        res=""
        m =  deepcopy(self.map.structure)

        for gIndex, gPath in enumerate(self.guardsPath):
            for i in range(1,len(gPath)-1):
                path = self.map.getPath(int(gPath[i-1]/self.map.getLength()), int(gPath[i-1]%self.map.getLength()), int(gPath[i]/self.map.getLength()), int(gPath[i]%self.map.getLength()))
                for node in path:
                    m[node[0]][node[1]] = "G" + str(gIndex)

        s = ""
        for row in self.map.structure:
            s += map.Case.WALL.value + map.Case.WALL.value 
        res+=(s + map.Case.WALL.value + map.Case.WALL.value)+"\n"
        # res+=(s + map.Case.WALL.value + map.Case.WALL.value)
        for i, row in enumerate(self.map.structure):
            s = ""
            for j, value in enumerate(row):
                if value == map.Case.PATH:
                    s += map.Case.PATH.value + map.Case.PATH.value
                elif value == map.Case.WALL:
                    s += map.Case.WALL.value + map.Case.WALL.value
                elif value != map.Case.GUARD:
                    s += value
            res+=(map.Case.WALL.value + s + map.Case.WALL.value)+"\n"
            # res+=(map.Case.WALL.value + s + map.Case.WALL.value)
        s = ""
        for row in self.map.structure:
            s += map.Case.WALL.value + map.Case.WALL.value 
        res+=(s + map.Case.WALL.value + map.Case.WALL.value)+"\n"
        # res+=(s + map.Case.WALL.value + map.Case.WALL.value)

        return res
    def printMapWithOneGuardsPath(self, idGuard):
        
        res=""
        m =  deepcopy(self.map.structure)

        gPath = self.guardsPath[idGuard]
        for i in range(1,len(gPath)-1):
            path = self.map.getPath(int(gPath[i-1]/self.map.getLength()), int(gPath[i-1]%self.map.getLength()), int(gPath[i]/self.map.getLength()), int(gPath[i]%self.map.getLength()))
            for node in path:
                m[node[0]][node[1]] = "G" + str(idGuard)

        s = ""
        for row in self.map.structure:
            s += map.Case.WALL.value + map.Case.WALL.value 
        res+=(s + map.Case.WALL.value + map.Case.WALL.value)+"\n"
        # print(s + map.Case.WALL.value + map.Case.WALL.value)
        for i, row in enumerate(m):
            s = ""
            for j, value in enumerate(row):
                if value == map.Case.PATH:
                    s += map.Case.PATH.value + map.Case.PATH.value
                elif value == map.Case.WALL:
                    s += map.Case.WALL.value + map.Case.WALL.value
                elif type(value) == map.Case:
                    s += value.value
                else:
                    s += value
            res+=(map.Case.WALL.value + s + map.Case.WALL.value)+"\n"
            # print(map.Case.WALL.value + s + map.Case.WALL.value)
        s = ""
        for row in self.map.structure:
            s += map.Case.WALL.value + map.Case.WALL.value 
        res+=(s + map.Case.WALL.value + map.Case.WALL.value)+"\n" 
        # print(s + map.Case.WALL.value + map.Case.WALL.value) 
        
        return res

    def copy(self):
        return Solution(self.map, self.numberOfGuards, self.guardsPath.copy())