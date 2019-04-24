#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:13:41 2019

@author: abhijithneilabraham
"""

import csv
import random
x=[]

'''
with open('people.csv', 'w+') as writeFile:
    writer = csv.writer(writeFile)
    for i in range(0,1376):
        
        line=[[random.randint(920,970)]]

        
  
        writer.writerows(line)   
'''
with open('final_dataset1.csv','r') as csvinput:
    with open('output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        for j in range(10248):
            
            all = []
            row = next(reader)
            print(row)
            
            row.append(0)
            all.append(row)
        
           
        

            writer.writerows(all)
with open('final_dataset2.csv','r') as csvinput:
    with open('output2.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        for j in range(1894):
            
            all = []
            row = next(reader)
            print(row)
            
            row.append(1)
            all.append(row)
        
           
        

            writer.writerows(all)

