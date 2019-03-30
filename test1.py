#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:13:41 2019

@author: abhijithneilabraham
"""

import csv
import random
lines=[]
lines2=[]
for i in range(0,10):
    lines.append(random.randint(920,970))
print(lines)
line=[lines,[0]]
csv.register_dialect("comma", delimiter=",")

with open('people.csv', 'w+') as writeFile:
    writer = csv.writer(writeFile,dialect="comma")
  
    writer.writerows(line)
   


