'''
Created on 7 May 2018

@author: User
'''


from random import randint
from KNeighboursClassifier import KNeighboursClassifier

def read_data(file_path):
    inData = []
    outData = []

    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            pair = line.split(" ")
            newLine=[]
            newLine.append(float(pair[0]))
            newLine.append(float(pair[1]))
            newLine.append(float(pair[2]))
            newLine.append(float(pair[3]))
            newLine.append(float(pair[4]))
            newLine.append(float(pair[5]))
            inData.append(newLine)
            outData.append(pair[6])

    return inData,outData


def __main__():
    inTrain, outTrain = read_data("column_2C.dat")

    inTest = []
    outTest = []
    
    for i in range(10):
        index = randint(0, len(inTrain))
    
        inTest.append(inTrain[index])
        outTest.append(outTrain[index])
    
        inTrain.remove(inTrain[index])
        outTrain.remove(outTrain[index])
    
    classifier = KNeighboursClassifier()
    
    classifier.fit(inTrain, outTrain)
    
    accuracy = 0
    
    for i in range(len(inTest)):
        if classifier.predict(inTest[i]) == outTest[i]:
            accuracy += 1
    
    print(float(accuracy) / len(inTest))


if __name__ == '__main__':
    __main__()