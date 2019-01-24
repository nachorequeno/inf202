#!/usr/bin/env python3
import numpy as np
from random import *

def zero():
    return ?

def unit():
    return ?

def somme(x,y):
    if ?:
        return zero()
    else:
        return unit()

def produit(x,y):
    if ?:
        return unit()
    else:
        return zero()

def union(R, S):
    RuS = []
    for ?:
        l = []
        for ?:
            if ? or ?:
                l.append(unit())
            else:
                l.append(zero())
        RuS.append(l)
    return RuS


def intersection(R, S):
    RiS = []
    for ?:
        l = []
        for ?:
            if ? and ?:
                l.append(unit())
            else:
                l.append(zero())
        RiS.append(l)
    return RiS
