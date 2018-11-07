'''
Created on 2 Jun 2018

@author: julia
'''
from Ruler import *
from Humidity import *
from Temperature import *
class Controller:
    def __init__(self, temperature, humidity):
        self.rules = Ruler()
        self.t = Temperature(temperature)
        self.h = Humidity(humidity)

    def run(self):
        agg = self.rules.evaluate(self.t, self.h)
        #print(agg)
        print(sorted(list(agg.items()), key = lambda x: x[1])[-1][0])