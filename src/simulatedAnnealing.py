# -*- coding: utf-8 -*-
"""
Created on Mon Oct 9 18:41:00 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.
"""

def search(t0, s0, tMin, eMax, deltaT = 0.1):
    t = t0 # initial temperature
    s = s0 # initial state
    e = energy(s)
    while T > Tmin and e > eMax:
        sN = neighbour(s)
        e = energy(sN)
        if eN < e or random() < exp(-(e - eN)/t):
            s = sN
            e = eN
        t = t - deltaT
    return s

def energy(s):
    return 1

def neighbour(s):
    return []