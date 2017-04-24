#!/usr/bin/env python
# coding=utf-8

# for bayes,
#   P(A/B) = P(B/A)*P(A)/P(B), A is class, B is predict data
# for naive, if P(B) const of x1x2x3..., then
#   P(B/A)=P(x1/A)P(x2/A)...
# P(A/B) = P(x1/A)*P(x2/A)...*P(A)/P(B), and just igore P(B)
def classify(trainData, trainLabel, predictData):

