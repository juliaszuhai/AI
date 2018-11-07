'''
Created on 27 Mar 2018

@author: User
'''
from random import randint
from Individ import Individ
class Population:
    
    def __init__(self,edges,vertexes,n):
        self.edges=edges
        self.vertexes=vertexes
        self.individs=self.getNewPopulation(n)
    
    def getNewPopulation(self,n):
        lista=[]
        for i in range(0,n):
            individ=Individ(len(self.edges))
            lista.append(individ)  
        return lista     
     
    def getLen(self):
        return len(self.individs) 
    
    
    def selectionTournament(self,n):
        strongParents = []
        for i in range(0,n):
            participants = []
            for j in range(3):
                idx = randint(0,len(self.individs)-1)
                p = self.individs[idx]
                participants.append((p,p.fitness(self.edges)))
            participants = sorted(participants,key=lambda p: p[1])
            strongParents.append(participants[0][0])
        
        return strongParents

    def selectionSurvival(self,children,n):
        for c in children:
            self.individs.append(c)
           
        strongParents = []
        for i in range(0,n):
            participants = []
            for j in range(3):
                idx = randint(0,len(self.individs)-1)
                p = self.individs[idx]
                participants.append((p,p.fitness(self.edges)))
            participants = sorted(participants,key=lambda p: p[1])
            strongParents.append(participants[0][0])
        
        self.individs = strongParents
    
    def __getitem__(self, key):
        return self.individs[key]
    def __setitem__(self,key,c):
        self.individs[key] = c
    def __str__(self):
        s = ""
        for i in range(self.getLen()):
            s += str(i)+" "+str(self.individs[i])+"->"+str(self.individs[i].fitness(self.edges))+"\n"
        return s