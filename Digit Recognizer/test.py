#!/usr/bin/env python
# coding=utf-8

import kNN, os
from numpy import *
from utils import *


def testDataSetSimple():
    trainData, trainLabel, testData, testLabel = kNN.loadDataSetSimple()
    for k in xrange(1,20,2):
        print "------------k: %d------------" % k
        predictResult = kNN.classify(trainData, trainLabel, testData, k)
        errorCount = 0
        testFile = os.listdir("dataSetSimple/testDigits")
        for i in xrange(len(testLabel)):
            if testLabel[i] != predictResult[i]:
                print "predict error: %s predict to be %d" % (testFile[i],
                        predictResult[i])
                errorCount += 1
        errorRate = float(errorCount) / len(testLabel)
        print "errorRate: %f\n" % errorRate


def testDataSetKaggle():
    trainData, trainLabel, testData= kNN.loadDataSetKaggle()

    # choose 1000 from train as test data
    trainLabel, testLabel = trainLabel[:-100], trainLabel[-100:-1]
    trainData, testData = trainData[:-100, :], trainData[-100:-1, :]

    for k in xrange(20,21): # k = 100
        print "------------k: %d------------" % k
        predictResult = kNN.classify(trainData, trainLabel, testData, k)
        errorCount = 0
        for i in xrange(len(testLabel)):
            if testLabel[i] != predictResult[i]:
                print "predict error: %d predict to be %d" % (testLabel[i],
                        predictResult[i])
                errorCount += 1
        errorRate = float(errorCount) / len(testLabel)
        print "the errorRate: %f\n" % errorRate
    return

def main():
    # testDataSetSimple()
    testDataSetKaggle()


if __name__=='__main__':
    main()


