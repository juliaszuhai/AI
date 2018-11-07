'''
Created on 19 Apr 2018

@author: User
'''

from Swarm import *
import math
from decimal import *

class Controller:
    def __init__(self, filename):
        self.filename=filename
        
    def iteration(self,neighbors):
        bestNeighbors=[]
        #determine the best neighbor for each particle
        for i in range(len(self.pop)):
            bestNeighbors.append(neighbors[self.pop[i]][0])
            for j in range(1,len(neighbors[self.pop[i]])):
                if (bestNeighbors[i].fitness > neighbors[self.pop[i]][j].fitness):
                    bestNeighbors[i]=neighbors[self.pop[i]][j]
                    
        #update the velocity for each particle
        for i in range(len(self.pop.population)):
            for j in range(len(self.pop[i].velocity)):
                newVelocity = self.w * self.pop.population[i].velocity[j]
                newVelocity = newVelocity + self.c1*random()*(bestNeighbors[i].pozition[j]-self.pop.population[i].pozition[j])    
                newVelocity = newVelocity + self.c2*random()*(self.pop.population[i].bestPozition[j]-self.pop.population[i].pozition[j])
                self.pop.population[i].velocity[j]=newVelocity
        
        #update the pozition for each particle
        for i in range(len(self.pop.population)):
            self.pop.updateParticle(i)
            
    
        

        
    def runAlg(self):
        self.edges,self.nodes=self.loadParameters()
        self.pop = Swarm(self.noParticles, self.edges,self.nodes)

        # we establish the particles' neighbors 
        neighborhoods=self.pop.selectNeighbours(self.sizeNeighbourhood)
        
        for i in range(100):
            self.iteration(neighborhoods)
            
    
        #print the best individual
        best = 0
        for i in range(1, len(self.pop)):
            if (self.pop[i].fitness<self.pop[best].fitness):
                best = i
            
        result = self.pop[best]
        fitnessOptim=self.pop[best].fitness
        e1,e2=[],[]
        n1,n2=set(),set()
        for i in range (0,len(result.pozition)):
            if result.pozition[i]==0:
                e1.append(self.edges[i])
                n1.add(self.edges[i][0])
                n1.add(self.edges[i][0])
            else:
                e2.append(self.edges[i])
                n2.add(self.edges[i][0])
                n2.add(self.edges[i][1])
                
        print(e1)
        print(e2)
        
        print("Fitness",fitnessOptim)
        individualOptim=self.pop.population[best].pozition
        print("Individual",individualOptim)
        
    
    
    def loadParameters(self):
        f = open(self.filename, "r")
        line = f.readline().strip()
        nodes=set()
        edges=[]
        while line != "":
            pair = line.split(" ")
            nodes.add(int(pair[0]))
            nodes.add(int(pair[1]))
            edges.append([int(pair[0]),int(pair[1])])     
            line = f.readline().strip()       
        f.close()
        self.noParticles=100
        self.sizeNeighbourhood=20
        self.w=1.0
        self.c1=1.0
        self.c2=2.5
        return edges,nodes
