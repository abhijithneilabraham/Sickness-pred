#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:13:41 2019

@author: abhijithneilabraham
"""

import csv
import random



with open('people.csv', 'w+') as writeFile:
    writer = csv.writer(writeFile)
    for i in range(0,1372):
        
        line=[[random.randint(920,970)]]
        
  
        writer.writerows(line)
        


