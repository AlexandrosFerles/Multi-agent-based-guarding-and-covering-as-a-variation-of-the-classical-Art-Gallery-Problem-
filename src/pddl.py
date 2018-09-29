# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:00:00 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.
"""
from model import map
import solution
import random

def getSolution(_map, _numberOfGuards):
    """
        This function returns a valid solution given a map, a number of guards
        The solution returns is not an optimal solution
    """
    guardsPath = [[] for i in range(_numberOfGuards)]
    S = solution.Solution(_map, _numberOfGuards, [])
    nodeAvailable = [i for i in range(0, _map.getLength() * _map.getLength() - 1)]

    # Init place
    for i,g in enumerate(_map.guards):
        x = g.locationX
        y = g.locationY
        if (x*_map.getLength()+y) in nodeAvailable:
            nodeAvailable.remove(x*_map.getLength()+y)
        guardsPath[i].append(x*_map.getLength()+y)

    while check(S) == False and len(nodeAvailable) > 0:
        i = random.randint(0, len(nodeAvailable) - 1)
        nodeChoose = nodeAvailable[i]
        nodeAvailable.pop(i)

        # Left
        if (nodeChoose-1) in nodeAvailable:
            nodeAvailable.remove(nodeChoose-1)
        # Right
        if (nodeChoose+1) in nodeAvailable:
            nodeAvailable.remove(nodeChoose+1)

        # Up
        if (nodeChoose-_map.getLength()) in nodeAvailable:
            nodeAvailable.remove(nodeChoose-_map.getLength())
        # Down
        if (nodeChoose+_map.getLength()) in nodeAvailable:
            nodeAvailable.remove(nodeChoose+_map.getLength())

        # Diagonal Up Left
        if (nodeChoose-_map.getLength()-1) in nodeAvailable:
            nodeAvailable.remove(nodeChoose-_map.getLength()-1)
        # Diagonal Up Right
        if (nodeChoose-_map.getLength()+1) in nodeAvailable:
            nodeAvailable.remove(nodeChoose-_map.getLength()+1)

        # Diagonal Down Left
        if (nodeChoose+_map.getLength()-1) in nodeAvailable:
            nodeAvailable.remove(nodeChoose+_map.getLength()-1)
        # Diagonal Down Right
        if (nodeChoose+_map.getLength()+1) in nodeAvailable:
            nodeAvailable.remove(nodeChoose+_map.getLength()+1)

        if _map.structure[int(nodeChoose/S.map.getLength())][int(nodeChoose%S.map.getLength())] == map.Case.PATH:
            g = random.randint(0, _numberOfGuards - 1)
            guardsPath[g].append(nodeChoose)
            #print("Assign node " + str(nodeChoose) + " to " + str(g))
    
        S.guardsPath = guardsPath
        

        # Finish round

    for g in S.guardsPath:
        g.append(g[0])

    # printCover(S)

    return S

def printCover(S):
    """
        This function prints the cover of the map
    """
    Map = [-1 for j in range(len(S.map.structure) * len(S.map.structure))]

    # From path of each guard build the map
    for guardId, guard in enumerate(S.guardsPath):
        for i in range(1, len(guard)-1):
            for node in S.map.getPath(int(guard[i-1]/S.map.getLength()), int(guard[i-1]%S.map.getLength()), int(guard[i]/S.map.getLength()), int(guard[i]%S.map.getLength())):
                Map = guardSaw(Map, S.map.getLength(), guardId, node[0]*S.map.getLength()+node[1])

    s = ""
    for row in S.map.structure:
        s += "##"
    print(s + "##")
    s = "#"
    for i, value in enumerate(Map):
        if value >= 0:
            s += str(value) + " "
        else:
            s += str(value)

        if i % (len( S.map.structure)) == 0:
            print(s + "#")
            s = "#"

    s = ""
    for row in S.map.structure:
        s += map.Case.WALL.value + map.Case.WALL.value
    print(s + "##")

def check(S):
    """
        Check if a solution is valid or not
        We check if Each point is seen and is seen by a guard
    """
    Map = [-1 for j in range(len(S.map.structure) * len(S.map.structure))]

    # remove obstacles
    for i, row in enumerate(S.map.structure):
        for j, value in enumerate(row):
            if value == map.Case.WALL:
                Map[i*S.map.getLength()+j] = -2

    # From path of each guard build the map
    for guardId, guard in enumerate(S.guardsPath):
        for i in range(1, len(guard)-1):
            for node in S.map.getPath(int(guard[i-1]/S.map.getLength()), int(guard[i-1]%S.map.getLength()), int(guard[i]/S.map.getLength()), int(guard[i]%S.map.getLength())):
                Map = guardSaw(Map, S.map.getLength(), guardId, node[0]*S.map.getLength()+node[1])

    for value in Map:
        if value == -1:
            return False

    return True

def guardSaw(_map, _sizeRealMap, _id, _position):
    """
        This function take map and add the id of the guard who visite a node for a given position
    """
    _map[_position] = _id

    # Left
    if _position-1 >= 0 and _position % _sizeRealMap != 1:
        _map[_position-1] = _id
    # Right
    if _position+1 < len(_map) and _position % _sizeRealMap != 0:
        _map[_position+1] = _id

    # Up
    if _position-_sizeRealMap >= 0:
        _map[_position-_sizeRealMap] = _id
    # Down
    if _position+_sizeRealMap < len(_map):
        _map[_position+_sizeRealMap] = _id

    # Diagonal Up Left
    if _position-_sizeRealMap-1 >= 0 and _position % _sizeRealMap != 1:
        _map[_position-_sizeRealMap-1] = _id
    # Diagonal Up Right
    if _position-_sizeRealMap+1 >= 0 and _position % _sizeRealMap != 0:
        _map[_position-_sizeRealMap+1] = _id

    # Diagonal Down Left
    if _position+_sizeRealMap-1 < len(_map) and _position % _sizeRealMap != 1:
        _map[_position+_sizeRealMap-1] = _id
    # Diagonal Down Right
    if _position+_sizeRealMap+1 < len(_map) and _position % _sizeRealMap != 0:
        _map[_position+_sizeRealMap+1] = _id

    return _map