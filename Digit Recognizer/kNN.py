#!/usr/bin/env python
# coding=utf-8
from numpy import *
from utils import *
import os
import operator


def classify(trainData, trainLabel, predictMatrix, k):
    predictResult = []
    j = 0
    for predictVec in predictMatrix:
        # calc oucilid distance
        distMatrix = trainData - predictVec
        distMatrix = distMatrix ** 2
        distSum = distMatrix.sum(axis=1)
        distSq = distSum ** 0.5

        # sort all distance
        sortedDistIndex = distSq.argsort()

        # choose k nearest neighbors
        classCount = {}
        for i in xrange(k):
            voteLabel = trainLabel[sortedDistIndex[i]]
            classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

        # sort classes in k nearest neighbors
        sortedClassIndex = sorted(classCount.iteritems(),
                                  key=operator.itemgetter(1), reverse=True)
        print "the %d data predict to be: %d" % (j, sortedClassIndex[0][0])
        j += 1
        # return the max voted class as predictResult
        predictResult.append(sortedClassIndex[0][0])
    return predictResult



def main():
    trainData, trainLabel, testData = loadDataSetKaggle()
    k = 10
    #predictResult = classify(trainData[0:1000, :], trainLabel[0:1000], testData[0:100, :], k)
    predictResult = classify(trainData, trainLabel, testData, k)
    genSubmission(predictResult)
    return


if __name__ == "__main__":
    main()
