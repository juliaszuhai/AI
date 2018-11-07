'''
Created on 1 Apr 2018

@author: User
'''
from Population import Population
from Problem import Problem
from random import random,randint
import matplotlib.pyplot as plt
import numpy as np

class Algorithm:
    def __init__(self):
        self.problem=Problem("input.txt")
        self.population=Population(self.problem.edges,self.problem.nodes,self.problem.dimPopulation)
    
    def iteration(self):
        children=[]
        selectedPopulation=self.population.selectionTournament(self.problem.dimPopulation // 2)
        for i in range(self.problem.dimPopulation // 4):
            i1=randint(0,len(selectedPopulation)-1)
            i2=randint(0,len(selectedPopulation)-1)
            if i1!=i2:
                c1,c2=selectedPopulation[i1].crossover(selectedPopulation[i2])
                c1.mutation(self.problem.pM)
                c2.mutation(self.problem.pM)
                children.append(c1)
                children.append(c2)
            else:
                i-=1
        
        self.population.selectionSurvival(children,self.problem.dimPopulation)
        #print(self.population)
        
    def run(self,nrIterations):
        means =[]
        standardDev=[]
        for i in range(0,nrIterations):
            self.iteration()
    
            fitnessValues = []
            for x in self.population.individs:
                fitnessValues.append((x,x.fitness(self.population.edges)))
            fitnessValues = sorted(fitnessValues,key=lambda p: p[1])
            
            fit =[]
            for f in fitnessValues:
                fit.append(f[1])
            result = fitnessValues[0][0]
            
            arr = np.array(fit)
            m = np.mean(arr, axis=0)
            means.append(m)
            
            
            stdDev=np.std(arr,axis=0)
            standardDev.append(stdDev)
            
        plt.plot(range(0,nrIterations),means,"r*")
        plt.plot(range(0,nrIterations),standardDev)
        plt.plot(range(0,nrIterations),fit,"go")
        plt.show()
        
        
        e1=[]
        e2=[]
        n1=set()
        n2=set()
        a=0
        for i in range (0,len(result.values)):
            if result.values[i]==0:
                e1.append(self.population.edges[i])
                n1.add(self.population.edges[i][0])
                n1.add(self.population.edges[i][0])
            else:
                e2.append(self.population.edges[i])
                n2.add(self.population.edges[i][0])
                n2.add(self.population.edges[i][1])
                
        print(e1)
        print(e2)
        return  fitnessValues[0][1]
    
    def statistics(self):
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    