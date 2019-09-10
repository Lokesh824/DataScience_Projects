# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:16:08 2019

@author: inkuml05
"""
import pandas as pd
import numpy as np
import operator

data = pd.read_csv('TShirtData.csv')


def calEucledianDistance(training, test, columnLength):
    distance = 0
    for x in range(columnLength):
        distance += np.square(training[x] - test[x])
    return np.sqrt(distance)

def KNN(training, test, k):
    distances = {}
    
    columnLength = test.shape[1]
    
    for x in range(len(training)):
        dis = calEucledianDistance(training.iloc[x], test, columnLength)
        distances[x] = dis[0]
        
    sorted_d = sorted(distances.items(), key = operator.itemgetter(1))       
    print('sorted values are ..', sorted_d)
    
    
    classVotes = {}
    Neighbours = []
    for x in range(k):
        Neighbours.append(sorted_d[0][0])
        
    for x in range(len(Neighbours)):
        labl = training.iloc[Neighbours[x]][-1]
        
        if labl in classVotes:
            
            classVotes[labl] += 1
        else:
                
            classVotes[labl] = 1
        
    finalAnswer = sorted(classVotes.items(), key = operator.itemgetter(1), reverse = True)
    
    return finalAnswer[0][0]
    
        
        
test = [[161,61]]

test = pd.DataFrame(test)

k =1
predection = KNN(data, test, k)
print('The size that will be the best match for customer is ...',predection)


