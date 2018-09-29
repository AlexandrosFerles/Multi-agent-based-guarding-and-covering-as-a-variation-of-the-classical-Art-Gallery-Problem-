# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:00:00 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.
"""

import random
import math
from enum import Enum
from model import guard
from collections import deque

class Case(Enum):
     PATH = " "
     WALL = "X"
     OBJECTS = "@"
     GUARD = "G"


class Map():
    __slot__ = ["structure",
                "guards",
                "adjacencesList"]

    def __init__(self,
                 _obstacles=0,
                 _objects=0,
                 _normalTimeout=-1,
                 _sizeX=20,
                 _sizeY=20,
                 _guards=2):

        self.structure = [[Case.PATH for _ in range(0, _sizeY)] for _ in range(0, _sizeX)]
        self.guards = [guard.Guard(self,
                             random.randint(0, _sizeX - 1),
                             random.randint(0, _sizeY - 1))
                       for _ in range(0, _guards)]

        for _ in range(_obstacles):
            while True:
                x = random.randint(0, _sizeX - 1)
                y = random.randint(0, _sizeY - 1)
                if self.is_empty(x,y):
                    self.structure[x][y] = Case.WALL
                    break

        for _ in range(_objects):
            while True:
                x = random.randint(0, _sizeX - 1)
                y = random.randint(0, _sizeY - 1)
                if self.is_empty(x,y):
                    self.structure[x][y] = Case.OBJECTS
                    break

        for g in self.guards:
            self.structure[g.locationX][g.locationY] = Case.GUARD

        self.createGraph()

    def createGraph(self):
        self.adjacencesList = []
        for i, row in enumerate(self.structure):
            for j, value in enumerate(row):
                p = i*self.getLength()+j
                neighbords = []
                # Left
                if j-1 >= 0 and self.structure[i][j-1] == Case.PATH: 
                    neighbords.append(p-1)
                # Right
                if j+1 < self.getLength() and self.structure[i][j+1] == Case.PATH: 
                    neighbords.append(p+1)

                # Up
                if i-1 >= 0 and self.structure[i-1][j] == Case.PATH: 
                    neighbords.append(p-self.getLength())
                # Down
                if i+1 < self.getLength() and self.structure[i+1][j] == Case.PATH: 
                    neighbords.append(p+self.getLength())

                # Diagonal Up Left
                if i-1 >= 0 and j-1 >= 0 and self.structure[i-1][j-1] == Case.PATH: 
                    neighbords.append(p-self.getLength()-1)
                # Diagonal Up Right
                if i-1 >= 0 and j+1 < self.getLength() and self.structure[i-1][j+1] == Case.PATH: 
                    neighbords.append(p-self.getLength()+1)

                # Diagonal Down Left
                if i+1 < self.getLength() and j-1 >= 0 and self.structure[i+1][j-1] == Case.PATH: 
                    neighbords.append(p+self.getLength()-1)
                # Diagonal Down Right
                if i+1 < self.getLength() and j+1 < self.getLength() and self.structure[i+1][j+1] == Case.PATH: 
                    neighbords.append(p+self.getLength()+1)

                self.adjacencesList.append(neighbords)

    def move(self,
             _guard,
             _x,
             _y):
        if self.is_empty(_x, _y):
            return self.guards[_guard].move(_x, _y)

        return False

    def is_empty(self,
                 _x,
                 _y):
        for guard in self.guards:
            if guard.locationX == _x or guard.locationY == _y:
                return False

        if self.structure[_x][_y] != Case.PATH:
            return False

        return True

    def printMap(self):

        res=""

        s = ""
        for row in self.structure:
            s += Case.WALL.value + Case.WALL.value 
        # print(s + Case.WALL.value + Case.WALL.value)
        res+=(s + Case.WALL.value + Case.WALL.value)+"\n"
        for i, row in enumerate(self.structure):
            s = ""
            for j, value in enumerate(row):
                if value == Case.PATH:
                    s += Case.PATH.value + Case.PATH.value
                elif value == Case.WALL:
                    s += Case.WALL.value + Case.WALL.value
                elif value == Case.GUARD:
                    for guardIndex, g in enumerate(self.guards):
                        if g.locationX == i and g.locationY == j:
                            s += Case.GUARD.value + str(guardIndex)
                else:
                    s += value.value
            # print(Case.WALL.value + s + Case.WALL.value)
            res+=(Case.WALL.value + s + Case.WALL.value)+"\n"
        s = ""
        for row in self.structure:
            s += Case.WALL.value + Case.WALL.value 
        # print(s + Case.WALL.value + Case.WALL.value)
        res+=(s + Case.WALL.value + Case.WALL.value)+"\n"

        return res


    def getPath(self,
                 xInit, 
                 yInit, 
                 xFinal, 
                 yFinal):
        start = xInit*self.getLength()+yInit
        end = xFinal*self.getLength()+yFinal

        distance = []
        pi = []
        colors = [] # 0: WHITE, 1: GRAY; 2: BLACK
        F = deque([start])

        # Init BFS
        for i in self.adjacencesList:
            if i == start:
                colors.append(1)
                distance.append(0)
            else:
                colors.append(0)
                distance.append(math.inf)
            pi.append(-1)


        # BFS
        while len(F) > 0:
            currentNode = F[0]
            F.popleft();
            for adj in self.adjacencesList[currentNode]:
                if colors[adj] == 0:
                    colors[adj] = 1
                    distance[adj] = distance[currentNode] + 1;
                    pi[adj] = currentNode;
                    F.append(adj);

            colors[currentNode] = 2
            if currentNode == end:
                break

        path = [[int(end/self.getLength()), int(end%self.getLength())]]
        current = end
        index = 0
        while current != start and index < len(self.adjacencesList):
            current = pi[current]
            if current == -1:
                return []
            path.append([int(current/self.getLength()), int(current%self.getLength())])
            index += 1
        
        return list(reversed(path))

    def getLength(self):
        return len(self.structure)