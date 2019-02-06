#!/usr/bin/env python3
import numpy as np
from random import *

def zero():
    return 0

def unit():
    return 1

def somme(x,y):
    if x==y==zero():
        return zero()
    else:
        return unit()

def produit(x,y):
    if x==y==unit():
        return unit()
    else:
        return zero()

def union(R, S):
    RuS = []
    for i in range(len(R)):
        l = []
        for j in range(len(R[i])):
            if R[i][j] == unit() or S[i][j] == unit():
                l.append(unit())
            else:
                l.append(zero())
        RuS.append(l)
    return RuS


def intersection(R, S):
    RiS = []
    for i in range(len(R)):
        l = []
        for j in range(len(R[i])):
            if R[i][j] == unit() and S[i][j] == unit():
                l.append(unit())
            else:
                l.append(zero())
        RiS.append(l)
    return RiS

