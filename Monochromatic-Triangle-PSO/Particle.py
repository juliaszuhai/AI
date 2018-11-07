'''
Created on 18 Apr 2018

@author: User
'''
from random import *

class Particle:
    def __init__(self,noEdges,edges):
        self.edges=edges
        self.pozition=self.individual(noEdges)
        self.evaluate()
        self.velocity=[ 0 for i in range(noEdges)]
        self.bestPozition=self.pozition.copy()
        self.bestFitness=self.fitness
        
    def evaluate(self):
        self.fitness=self.fit(self.pozition)
        
    def individual(self,noEdges):
        e1=[]
        for i in range(0,noEdges):
            r=random()
            if r < 0.5:
                e1.append(0)
            else:
                e1.append(1)
        return e1   
     
    def fit(self,lista):
        allVertexes = set()
        for e in self.edges:
            allVertexes.add(e[0])
            allVertexes.add(e[1])
        e1=[]
        e2=[]
        n1=set()
        n2=set()
        a=0
        for i in range (0,len(lista)):
            if lista[i]==0:
                e1.append(self.edges[i])
                n1.add(self.edges[i][0])
                n1.add(self.edges[i][1])
            else:
                e2.append(self.edges[i])
                n2.add(self.edges[i][0])
                n2.add(self.edges[i][1])
        for x in n1:
            for y in n1:
                for z in n1:
                    if [x,y] in e1 and [y,z] in e1 and [x,z] in e1:
                        a += 1
        for x in n2:
            for y in n2:
                for z in n2:
                    if [x,y] in e2 and [y,z] in e2 and [x,z] in e2:
                        a += 1
                        
        d1 = len(allVertexes.difference(n1))
        d2 = len(allVertexes.difference(n2))
        a += d1
        a += d2 
                   
        return a  
     
    def getPosition(self):
        return self.postion
    
    def getVelocity(self):
        return self.velocity
    
    def getBestPosition(self):
        return self.bestPozition
    
    def getBestFitness(self):
        return self.bestFitness 
    
    def update(self,newPozition):
        self.pozition=newPozition.copy()
        self.evaluate()
        if self.fitness<self.bestFitness:
            self.bestFitness=self.fitness
            self.bestPozition=self.pozition 
            
    def __getitem__(self, key):
        return self.values[key]
    def __setitem__(self,key,c):
        self.values[key] = c
    def __str__(self):
        return "("+str(self.values)+")"       