# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:00:00 2017

@author: Chastel F., Ferles A., Matsoukas C., Vecchio Q., Zervakis G.
"""

class Guard():
    __slot__ = ["map",
                "view",
                "speedness",
                "tiredness",
                "locationX",
                "locationY"]

    def __init__(self,
                 _map,
                 _locationX,
                 _locationY,
                 _view = 2,
                 _speedness = 1,
                 _tiredness = 0):
        self.map = _map
        self.view = _view
        self.speedness = _speedness
        self.tiredness = _tiredness
        self.locationX = _locationX
        self.locationY = _locationY

    def reset(self):
        self.tiredness += self.speedness/3

    def isTired(self,
                _maxtired = 10):
        if self.tiredness >= _maxtired:
            return True
        else:
            return False

    def move(self,
             _x,
             _y):
        difference_x = self.locationX - _x
        difference_y = self.locationY - _y

        if difference_x == 0 and difference_y == 0 and self.tiredness >= 0:
            self.tiredness -= 3

            if self.tiredness < 0:
                self.tiredness = 0

        if (difference_x and difference_y) in [-self.speedness, 0, self.speedness]:
            self.locationX = _x
            self.locationY = _y
            se
            return True

        return False

    def inView(self):
        pass

    def path_indexed(self,
                     _index):
        return self.path(int(_index / len(self.map)), int(_index % len(self.map)))


