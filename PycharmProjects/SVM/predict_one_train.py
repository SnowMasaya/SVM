#!/usr/bin/env python
from math import exp

class predictOnePython:
    
    def __init__(self, weight, phi):
        self.weight = weight
        self.phi = phi
        self.score = 0

    def predict(self):
        for name,value in self.phi.iteritems():
            if self.weight[name]:
               score = score + value * self.weight[name]
        self.score =  exp(score) / (1 + exp(score))
        return self.score
