#!/usr/bin/env python
# coding=utf-8

import kNN, os
import LogisticRegression as LR
import numpy as np
from utils import *


def testKnnSimple():
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


def testKnnKaggle():
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

def testLRSimple(trainAgain):
    trainData, trainLabel, testData, testLabel = kNN.loadDataSetSimple()

    # Add bais 1 in Xi
    baisVec = np.ones(len(trainData))
    trainData = np.concatenate((baisVec, trainData), axis=1)

    # just get 0 and 1 data
    index01 = [index01 for (index01, val) in enumerate(trainLabel) if val == 1
            or val == 0]
    trainData = trainData[index01]
    trainLabel = trainLabel[index01]

    if trainAgain:
        thetaVec = LR.trainLogisticRegression(trainData, trainLabel, 0.01,
                100)
    else :
        thetaVec = np.ones(len(trainData[0]))

    predictResult = LR.classify(theraVec, testData)

    errorCount = 0
    testFile = os.listdir("dataSetSimple/testDigits")
    for i in xrange(len(testLabel)):
        if testLabel[i] != predictResult[i]:
            print "predict error: %s predict to be %d" % (testFile[i],
                    predictResult[i])
            errorCount += 1
    errorRate = float(errorCount) / len(testLabel)
    print "errorRate: %f\n" % errorRate


def main():
    # testKnnSimple()
    # testKnnKaggle()

    testLRSimple(True)

if __name__=='__main__':
    main()


