'''
Created on 18 Apr 2018

@author: User
'''
from Particle import *
from Controller import *
import math


class Swarm:
    def __init__(self,n,edges,vertex):
        self.edges=edges
        self.vertex=vertex
        self.noEdges=len(self.edges)
        self.sizePop=n
        self.population=self.newSwarm()
        
    def newSwarm(self):
        return [Particle(self.noEdges,self.edges) for x in range(self.sizePop)]
    
    def getBestNeighbour(self):
        return self.getBestKParticles(1)
    
    
    def getBestKParticles(self,k):
        a= sorted(self.population, key=lambda x: x.fitness)
        return a[:k]
        
    
    def selectNeighbours(self,nSize):
        neighbours={}
        for i in range(len(self.population)):
            localNeighbour=[]
            for j in range(nSize):
                x=randint(0, len(self.population)-1)
                while (x in localNeighbour):
                    x=randint(0, len(self.population)-1)
                localNeighbour.append(self.population[x])
            neighbours[self.population[i]] = localNeighbour.copy()
        print("neighbours:",neighbours)
        return neighbours
    
    def __getitem__(self, key):
        return self.population[key]
    def __setitem__(self,key,c):
        self.population[key] = c
    def __len__(self):
        return len(self.population)
    
    #sigmoid function
    def sigmoid(self,x):
        return 1 / (1 + math.exp(-x))
    
    #update the pozition for each particle
    def updateParticle(self,i):
        newPozition=[]
        for j in range(len(self.population[i].velocity)):
            willChange = self.sigmoid(self.population[i].velocity[j])
            if willChange < 0.5:
                newPozition.append(self.population[i].pozition[j])
            else:
                newPozition.append(self.population[i].bestPozition[j])                   
        self.population[i].update(newPozition)
    
        
            
        
        
        
 
                
    
          
        