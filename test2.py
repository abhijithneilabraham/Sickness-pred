#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:18:10 2019

@author: abhijithneilabraham
"""
from numpy import array
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
dataset = numpy.loadtxt("dataset.csv", delimiter=",")
X = dataset[:,0]
Y = dataset[:,1]
# create model
model = Sequential()
#model.add(Dense(12, input_dim=1, activation='relu'))
n_steps=1
n_features=1
print(X)
x=array(X)
x1 = x.reshape((len(x), n_steps, n_features))

model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))

model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(x1, Y, epochs=150, batch_size=10)
# evaluate the model
scores = model.evaluate(x1, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
predictions = model.predict(x1)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)
