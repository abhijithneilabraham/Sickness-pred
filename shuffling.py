#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 00:42:10 2019

@author: abhijithneilabraham
"""
import csv
from random import shuffle
ip=open('dataset.csv','r')
data=ip.readlines()
print(data)
shuffle(data)
print(data)


with open('1.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(data)
