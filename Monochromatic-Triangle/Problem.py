'''
Created on 29 Mar 2018

@author: User
'''

class Problem:        
    def __init__(self,fileName):
        self.edges= []
        self.nodes = set()
        self.n = 0 
        self.dimPopulation=0
        self.pM=0.01
        self.loadData(fileName)
    
    def loadData(self,fileName):
        f = open(fileName, "r")
        self.dimPopulation=int(f.readline().strip())
        self.pM=float(f.readline().strip())
        line = f.readline().strip()
        while line != "":
            pair = line.split(" ")
            self.nodes.add(int(pair[0]))
            self.nodes.add(int(pair[1]))
            self.edges.append([int(pair[0]),int(pair[1])])     
            line = f.readline().strip()       
        f.close()
        return len(self.nodes)
        