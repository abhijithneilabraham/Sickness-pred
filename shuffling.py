#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 00:42:10 2019

@author: abhijithneilabraham
"""
import csv
import numpy
from random import shuffle
import matplotlib.pyplot as plt
patients=['anas.csv','bristo.csv','christy.csv','raees.csv','suresh.csv','abnormal.csv']
for i in patients:
    data=numpy.loadtxt(i, delimiter=",")
    plt.plot(data)
    i=i[:-4]
    print(i)
    plt.ylabel('EMG Signal')
    plt.show()
