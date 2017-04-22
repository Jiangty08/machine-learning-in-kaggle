#!/usr/bin/env python
# coding=utf-8

import kNN, os
from numpy import *


def testDataSet1():
    trainMatrix, trainLabel, testMatrix, testLabel = kNN.loadDataSet1()
    for k in xrange(1,20,2):
        print "------------k: %d------------" % k
        predictResult = kNN.classify(array(trainMatrix), trainLabel, testMatrix, k)
        errorCount = 0
        testFile = os.listdir("dataSet1/testDigits")
        for i in xrange(len(testLabel)):
            if testLabel[i] != predictResult[i]:
                print "predict error: %s predict to be %d" % (testFile[i],
                        predictResult[i])
                errorCount += 1
        errorRate = float(errorCount) / len(testLabel)
        print "errorRate: %f\n" % errorRate


def testDataSet2():
    return

def main():
    testDataSet1()
    # testDataSet2()


if __name__=='__main__':
    main()


