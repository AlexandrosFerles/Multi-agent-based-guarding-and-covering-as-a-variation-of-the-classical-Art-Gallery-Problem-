# -*- coding: utf-8 -*-


class Visualizer():
    __slot__= ["binding"]

    def __init__(self,
                 _binding):
        self.binding = _binding

    def visualize(self,
                  _fields):
        for field in _fields:
            print(self._transform(_field=field))

    def _transform(self,
                   _field,
                   _binding=self.binding):
        result = []
        for line in _field:
            result.append([_binding[k] for k in line])

        return result