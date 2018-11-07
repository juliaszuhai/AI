'''
Created on 1 Apr 2018

@author: User
'''
from Algorithm import Algorithm
from Individ import Individ
import matplotlib.pyplot as plt

def main():
    a = Algorithm()
    return a.run(100)
    '''a=[1,2,3,4,5,6,7,8,9,10]
    b=['a','b','c','d','e','f','g','h','i','j']
    a1=Individ(8)
    a1.values=a
    b1=Individ(8)
    b1.values=b
    
    print("parinte1:",a)
    print("parinte2:",b)
    c1,c2=a1.crossover(b1)
    print("copil1:",c1)
    print("copil2",c2)'''

if __name__ == '__main__':
    """results = []
    for i in range(30):
        print(i)
        result = main()
        results.append(result)
    plt.plot(range(0,30),results)
    plt.show()
    """
    result = main()