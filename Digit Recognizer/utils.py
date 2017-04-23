#!/usr/bin/env python
# coding=utf-8

from numpy import *
import os

# change output.csv start from 0 to 1
def formatOutput():
    outFile = file("dataSetKaggle/output.csv")
    newOutFile = open("dataSetKaggle/newout.csv", 'w')
    lines = outFile.readlines()
    newOutFile.write(lines[0])
    lines.remove(lines[0])
    for line in lines:
        res = line.split(',')
        newOutFile.write("%d,%d\n" % (int(res[0])+1, int(res[1])))
    newOutFile.close()

# kaggle digit dataSet
def loadDataSetKaggle():
    trainMatrix = []
    testMatrix = []
    trainFile = "dataSetKaggle/train.csv"
    testFile = "dataSetKaggle/test.csv"

    lines = file(trainFile).readlines()
    lines.remove(lines[0])
    for line in lines:
        trainMatrix.append([int(x) for x in line.strip("\r\n").split(",")])
    trainMatrix = array(trainMatrix)

    trainLabel = trainMatrix[:, 0]
    trainData = trainMatrix[:, 1:]

    lines = file(testFile).readlines()
    lines.remove(lines[0])
    for line in lines:
        testMatrix.append([int(x) for x in line.strip("\r\n").split(",")])

    return trainData, trainLabel, array(testMatrix)

# a simple dataSet
def loadDataSetSimple():
    trainData = []
    trainLabel = []
    testData = []
    testLabel = []
    trainDir = "dataSetSimple/trainingDigits"
    testDir = "dataSetSimple/testDigits"
    for trainFile in os.listdir(trainDir):
        trainData.append(file2Vec(file(os.path.join(trainDir, trainFile))))
        trainLabel.append(int(trainFile[0]))
    for testFile in os.listdir(testDir):
        testData.append(file2Vec(file(os.path.join(testDir, testFile))))
        testLabel.append(int(testFile[0]))
    return array(trainData), trainLabel, testData, testLabel


def file2Vec(imgFile):
    returnVec = []
    for line in imgFile.readlines():
        returnVec.extend([int(x) for x in list(line)[:-1]])
    return returnVec


def genSubmission(predictResult):
    outFile = open("dataSetKaggle/output.csv", 'w')
    outFile.write("ImageId,Label\n")
    for i in xrange(len(predictResult)):
        outFile.write("%d,%d\n" % (i+1, predictResult[i]))
    outFile.close()

