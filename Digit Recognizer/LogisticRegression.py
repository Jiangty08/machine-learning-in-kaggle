#!/usr/bin/env python
# coding=utf-8

from numpy import *

########################################################
# logistic regression for 2 classify
########################################################
def classify(thetaVec, predictData):
    predictResult = []
    for inputX in predictData:
        y = sigmoid(mat(inputX)*(mat(thetaVec).T))
        predictResult.append(round(y))
    return predictResult

def

# rtype: thetaVec
def trainLogisticRegression(trainData, trainLabel, rate, totalCycle):
    trainX = mat(trainData)
    trainY = mat(trainLabel)
    thetaVec = np.ones(len(trainData[0]))

    for i in xrange(totalCycle):
        thetaVec, cost = gradientDescent(thetaVec, trainX, trainY, rate)
        print "the %d iter, cost is %f" % (i, cost)

    return thetaVec

# Cost(h(x),y) = -ylog(h(x)) - (1-y)log(1-h(x))
def costFunction(inputX, label, thetaVec):
    hx = mat(inputX)*(mat(thetaVec).T)
    y = outputY[i]
    cost = -y*log(hx) - (1-y)log(1-hx)
    return cost

# For gradient descent algorithm:
#   theta = theta - rate * J'/theta'
# after deduction, we get very simple formula:
#   thetaVec = thetaVec - rate * (Hx - Y).T * X
# 1 x m : Hx.T, Y.T
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
    thetaVec = thetaVec - rate * (Hx - Y).T * X
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
def costFunctionMulti(inputX, label, thetaMatrix):
    outputY = zeros(classNum)
    outputY[label+1] = 1
    i = 0
    for thetaVec in thetaMatrix:
        hx = mat(inputX)*(mat(thetaVec).T)
        y = outputY[i]
        cost = -y*log(hx) - (1-y)log(1-hx)
        outputY[i] -= sigmoid(cost))
        i ++
    return sum(outputY)


def gradientDescentMulti(thetaMatrix, trainData, trainLabel, rate):
    return thetaMatrix

# rtype: thetaVec
def trainLogisticRegressionMulti(trainData, trainLabel, rate, totalCycle):
    trainX = mat(trainData)
    trainY = mat(trainLabel)
    for i in xrange(totalCycle):
        thetaVec, cost = gradientDescent(thetaVec, trainX, trainY, rate)
        print "the %d iter, cost is %f" % (i, cost)

    return thetaVec

def sigmoid(intX):
    return 1.0/(1+exp(-intX))


