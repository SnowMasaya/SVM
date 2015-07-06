#!/usr/bin/env python
from math import exp,pow

class updatePython:
    
    def __init__(self, weight, phi, y, sampling_number):
        self.weight = weight
        self.phi = phi
        self.y = y
        self.alpha = 1.0 * 1.0 / (4.0 + sampling_number)

    def update(self):
        for name,value in self.phi.iteritems():
            if int(self.y) >= 0:
                self.weight[name] =  float(self.weight[name]) + 1.0 * self.alpha * \
                                                               updatePython.diff_function(self, name, value)
            else:
                self.weight[name] =  float(self.weight[name]) + -1.0 * self.alpha * \
                                                                      updatePython.diff_function(self, name, value)
        return self.weight

    @staticmethod
    def diff_function(self, name, value):
        diff_value = 0
        diff_value = value * 1.0 * exp(value * self.weight[name]) / pow((1 + exp(value * self.weight[name])), 2)
        return diff_value
