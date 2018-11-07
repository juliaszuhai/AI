'''
Created on 27 Mar 2018

@author: User
'''
from random import random, randint
class Individ:
    def __init__(self,nrEdges):
        self.values=self.individual(nrEdges)
     
    def getLen(self): 
        return len(self.values)
      
    def individual(self,nrEdges):
        e1=[]
        for i in range(0,nrEdges):
            r=random()
            if r < 0.5:
                e1.append(0)
            else:
                e1.append(1)
        return e1
                
    
    def mutation(self,pm):
        r=random()
        if r > pm:
            i=randint(0,len(self.values)-1)
            self.values[i]=1-self.values[i]
        
    
    def fitness(self,lista):
        allVertexes = set()
        for e in lista:
            allVertexes.add(e[0])
            allVertexes.add(e[1])
        e1=[]
        e2=[]
        n1=set()
        n2=set()
        a=0
        for i in range (0,len(self.values)):
            if self.values[i]==0:
                e1.append(lista[i])
                n1.add(lista[i][0])
                n1.add(lista[i][1])
            else:
                e2.append(lista[i])
                n2.add(lista[i][0])
                n2.add(lista[i][1])
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
        
    
    def crossover(self, individ):
        '''2 cut mutation'''
        n1=randint(0,len(self.values)/2)
        n2=randint(n1,len(self.values))
        c1=[]
        c2=[]
        for i in range(0,n1):
            c1.append(self.values[i])
            c2.append(individ[i])
        for i in range(n1,n2):
            c1.append(individ[i])
            c2.append(self.values[i])
        for i in range(n2,len(self.values)):
            c1.append(self.values[i])
            c2.append(individ[i])  
            
        child1 = Individ(self.getLen())
        child1.values = c1
        child2 = Individ(self.getLen())
        child2.values = c2
        return child1,child2
    
    def __getitem__(self, key):
        return self.values[key]
    def __setitem__(self,key,c):
        self.values[key] = c
    def __str__(self):
        return "("+str(self.values)+")"