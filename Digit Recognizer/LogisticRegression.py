#!/usr/bin/env python
# coding=utf-8

from numpy import *

########################################################
# logistic regression for 0-1 classify
########################################################
def classify(thetaVec, X):
    """
    Using Logistic regression to classify data

    Parameters
    ----------
    thetaVec    : list or ndarray
        Params of LR model
    X           : list or ndarray
        Input data to predict

    Returns
    -------
    Y           : list
        Predict result of input data
    """
    Y = []
    for xi in X:
        y = sigmoid(mat(xi)*(mat(thetaVec).T))
        y = sum(y) # mat to float
        Y.append(round(y))
    return Y

def trainLogisticRegression(X, Y, rate, cycles):
    """
    Train logistic regression model

    Parameters
    ----------
    X   : list or ndarray
        Params of LR model
    Y   : list or ndarray
        Input data to predict

    Returns
    -------
    Y           : list
        Predict result of input data
    """
    thetaVec = zeros(len(trainData[0]))

    for i in xrange(totalCycle):
        thetaVec, cost = gradientDescent(thetaVec, trainData, trainLabel, rate)
        print "the %d iter, cost is %f" % (i, cost)
        print "the %d iter, thetaVec is %r" % (i, thetaVec)

    return thetaVec

# Cost(h(x),y) = -ylog(h(x)) - (1-y)log(1-h(x))
def costFunction(inputX, label, thetaVec):
    hx = mat(inputX)*(mat(thetaVec).T)
    hx = sum(hx)
    hx = sigmoid(hx)
    y = float(label)
    cost = -y*log(hx) - (1-y)*log(1-hx)
    return cost

# For gradient descent algorithm:
#   theta = theta - rate * J'/theta'
# after deduction, we get very simple formula:
#   thetaVec = thetaVec - rate * (Hx - Y).T * X
# 1 x m : Hx, Y
# 1 x n : thetaVec
# m x n : X
# m     : means trainData size is m
# n     : means features num is n
def gradientDescent(thetaVec, trainData, trainLabel, rate):
    Hx = []
    cost = 0.0
    for i in xrange(len(trainLabel)):
        h = costFunction(trainData[i], trainLabel[i], thetaVec)
        Hx.append(h)
        cost += h
    Hx = mat(Hx)
    X = mat(trainData)
    Y = mat(trainLabel)
    thetaVec = thetaVec - rate * (Hx - Y) * X
    return thetaVec, cost




########################################################
# logistic regression for multi classify
########################################################
classNum = 10

def classifyMulti(thetaMatrix, predictData):
    predictResult = []
    for inputX in predictData:
        outputY = []
        for thetaVec in thetaMatrix:
            y = mat(inputX)*(mat(thetaVec).T)
            outputY.append(sigmoid(y))
        predictResult.append(outputY.index(max(outputY)))
    return predictResult

# Cost(h(x),y) = -ylog(h(x)) - (1-y)log(1-h(x))
# inputX: 1 x n
# labelY: 1 x k
# thetaMatrix: k x n
# cost  : 1 x k
def costFunctionMulti(inputX, labelY, thetaMatrix):

    Hx = mat(inputX)*(mat(thetaMatrix).T)
    Hx = sigmoid(Hx)
    cost = -labelY*log(Hx.A) - (1-labelY)*log(1-Hx.A)

    return cost


# For gradient descent algorithm:
#   theta = theta - rate * J'/theta'
# after deduction, we get very simple formula:
#   thetaVec = thetaVec - rate * (Hx - Y).T * X
# m x k : Hx
# m x n : X
# m x k : Y
# k x n : thetaMatrix
# m     : means trainData size is m
# n     : means features num is n
# k     : means classes num is k
def gradientDescentMulti(thetaMatrix, trainData, trainLabel, rate):
    Hx = []
    cost = 0.0
    for i in xrange(len(trainLabel)):
        h = costFunctionMulti(trainData[i], trainLabel[i], thetaMatrix)
        Hx.append(h)
        cost += h
    Hx = mat(Hx)
    X = mat(trainData)
    Y = mat(trainLabel)
    thetaMatrix = thetaMatrix- rate * (Hx - Y).T * X
    return thetaMatrix, cost


# rtype: thetaVec
def trainLogisticRegressionMulti(trainData, trainLabel, rate, totalCycle):
    classNum = len(set(trainLabel))
    trainX = mat(trainData)
    trainY = zeros(len(trainLabel), classNum)
    for i in xrange(len(trainLabel)):
        trainY[i][trainLabel[i]] = 1


    for i in xrange(totalCycle):
        thetaMatrix, cost = gradientDescent(thetaMatrix, trainX, trainY, rate)
        print "the %d iter, cost is %f" % (i, cost)

    return thetaMatrix

def sigmoid(intX):
    return 1.0/(1+exp(-intX))


