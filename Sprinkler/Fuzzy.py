'''
Created on 2 Jun 2018

@author: julia
'''
import numpy as np

class Fuzzy:
    def __init__(self):
        self.labels = {}
        self.value = 0

    def toDiscrete(self):
        ret = {}
        graph = self.labels
        value = self.value
        for key in graph.keys():
            #print(key)
            for i in range(len(graph[key]) - 1):
                if graph[key][i][0] <= value and value <= graph[key][i + 1][0]:
                    if graph[key][i][0] == -np.inf:
                        ret[key] = graph[key][i][1]
                        continue
                    if graph[key][i + 1][0] == np.inf:
                        ret[key] = graph[key][i + 1][1]
                        #print(ret[key])
                        continue
                    deltaY = graph[key][i + 1][1] - graph[key][i][1]
                    deltaX = graph[key][i + 1][0] - graph[key][i][0]
                    ret[key] = graph[key][i][1] + ((value - graph[key][i][0]) / deltaX) * deltaY
        return ret


