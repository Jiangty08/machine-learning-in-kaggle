#!/usr/bin/env python
# coding=utf-8

import numpy as np
import os


def formatOutput(name="dataSetKaggle/output.csv"):
    """
    Format kaggle submission file inplace, start from 0 to start from 1

    Parameters
    ----------
    name : string
        Path of file which to be formatted. Default is "dataSetKaggle/output.csv".

    """
    f = file(name)
    lines = f.readlines()
    f.close()

    with open(name, 'w') as f
        f.write(lines[0])
        lines.remove(lines[0])
        for line in lines:
            ll = line.split(',')
            f.write("%d,%d\n" % (int(res[0]) + 1, int(res[1])))


def loadDataSetKaggle(trainFile="dataSetKaggle/train.csv", testFile="dataSetKaggle/test.csv"):
    """
    Load Data Set from Kaggle

    Parameters
    ----------
    trainFile   : string
        Path of file contains traindata set.
    testFile    : string
        Path of file contains test data set.

    Returns
    -------
    trainX  : ndarray
        Input data of train data set
    trainY  : ndarray
        Label of train data set
    testX   : ndarray
        Input data of test data set
    """
    trainMatrix = []
    testMatrix = []

    with open(trainFile) as openFile:
        lines = openFile.readlines()
        lines.remove(lines[0])
        for line in lines:
            trainMatrix.append([int(x) for x in line.strip("\r\n").split(",")])
        trainMatrix = array(trainMatrix)

    trainY = trainMatrix[:, 0]
    trainX = trainMatrix[:, 1:]

    with open(testFile) as openFile:
        lines = openFile.readlines()
        lines.remove(lines[0])
        for line in lines:
            testMatrix.append([int(x) for x in line.strip("\r\n").split(",")])
    testX = np.array(testMatrix)

    return trainX, trainY, testX


def loadDataSetSimple(trainDir="dataSetSimple/trainingDigits", testDir="dataSetSimple/testDigits"):
    """
    Load Data Set from Kaggle

    Parameters
    ----------
    trainDir    : string
        Path of directories contains traindata set.
    testDir     : string
        Path of directories contains test data set.

    Returns
    -------
    trainX  : ndarray
        Input data of train data set
    trainY  : ndarray
        Labels of train data set
    testX   : ndarray
        Input data of test data set
    testY   : ndarray
        labels of test data set
    """
    trainData  = []
    trainLabel = []
    testData   = []
    testLabel  = []
    for trainFile in os.listdir(trainDir):
        with open(os.path.join(trainDir, trainFile)) as openFile:
            trainData.append(file2Vec(openFile))
            trainLabel.append(int(trainFile[0]))
    for testFile in os.listdir(testDir):
        with open(os.path.join(testDir, testFile)) as openFile:
            testData.append(file2Vec(openFile))
            testLabel.append(int(testFile[0]))
    trainX, trainY = array(trainData), array(trainLabel)
    testX, testY = array(testData), array(testLabel)

    return trainX, trainY, testX, testY



def file2Vec(imgFile):
    """
    Convert the imgFile which contains image info, to a vector

    Parameters
    ----------
    imgFile : file object
        Opened file of image

    Returns
    -------
    imgVec  : ndarray
        Vector contains imgae info, ndim = 1
    """
    imgVec = []
    for line in imgFile.readlines():
        imgVec.extend([int(x) for x in list(line)[:-1]])
    return imgVec


def genSubmission(predictResult, name = "dataSetKaggle/output.csv"):
    """
    Generate kaggle submission file, using predictResult

    Parameters
    ----------
    predictResult : ndarray or list
        Predict Result of test data set

    Returns
    -------
    imgVec  : ndarray
        Vector contains imgae info, ndim = 1
    """
    with open(name, 'w') as outFile
        outFile.write("ImageId,Label\n")
        for i in xrange(len(predictResult)):
            outFile.write("%d,%d\n" % (i + 1, predictResult[i]))
