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
    for i in range(0,1376):
        
        line=[[random.randint(920,970)]]
        
  
        writer.writerows(line)
        
with open('people.csv','r') as csvinput:
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('0')
        all.append(row)

        for row in reader:
            row.append(row[0])
            all.append(row)

        writer.writerows(all)

