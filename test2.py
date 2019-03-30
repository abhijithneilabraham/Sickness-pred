#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:18:10 2019

@author: abhijithneilabraham
"""
import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# fix random seed for reproducibility
numpy.random.seed(7)
# load the dataset
dataframe = pandas.read_csv('final.csv', usecols=[0], engine='python', skipfooter=3)
dataset = dataframe.values
print(len(dataset))
dataframe2 = pandas.read_csv('people.csv', usecols=[0], engine='python', skipfooter=3)
dataset2 = dataframe2.values
print(len(dataset2))