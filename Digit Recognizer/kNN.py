#!/usr/bin/env python
# coding=utf-8
from numpy  import *
import os, operator

def classify(trainMatrix, trainLabel, predictMatrix, k):
    predictResult = []
    for predictVec in predictMatrix:
        distMatrix = trainMatrix - predictVec
        distMatrix = distMatrix ** 2
        distSum = distMatrix.sum(axis=1)
        distSq = distSum ** 0.5
        sortedDistIndex = distSq.argsort()
        classCount = {}
        for i in xrange(k):
            voteLabel = trainLabel[sortedDistIndex[i]]
            classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
        sortedClassIndex = sorted(classCount.iteritems(),
                key=operator.itemgetter(1), reverse=True)
        predictResult.append(sortedClassIndex[0][0])
    return predictResult


# kaggle digit dataSet
def loadDataSet2():
    return

# a simple dataSet
def loadDataSet1():
    trainMatrix = []
    trainLabel = []
    testMatrix = []
    testLabel = []
    trainDir = "dataSet1/trainingDigits"
    testDir = "dataSet1/testDigits"
    for trainFile in os.listdir(trainDir):
        trainMatrix.append(file2Vec(file(os.path.join(trainDir, trainFile))))
        trainLabel.append(int(trainFile[0]))
    for testFile in os.listdir(testDir):
        testMatrix.append(file2Vec(file(os.path.join(testDir, testFile))))
        testLabel.append(int(testFile[0]))
    return trainMatrix, trainLabel, testMatrix, testLabel

def file2Vec(imgFile):
    returnVec = []
    for line in imgFile.readlines():
        returnVec.extend([int(x) for x in list(line)[:-1]])
    return returnVec

if __name__ == "__main__":
    main()

def main():
    return

