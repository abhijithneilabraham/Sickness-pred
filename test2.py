#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:18:10 2019

@author: abhijithneilabraham
"""
from numpy import array 
import pandas
import math
import random
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# fix random seed for reproducibility
numpy.random.seed(42)
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

model.add(LSTM(10, activation='relu',kernel_initializer='random_normal', input_shape=(n_steps, n_features)))

model.add(Dense(4, kernel_initializer='random_normal', activation='relu'))
	# Compile model
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# Fit the model
model.fit(x1, Y, epochs=20, batch_size=10)
# evaluate the model
scores = model.evaluate(x1, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
test1 = numpy.loadtxt("abnormal.csv", delimiter=",")
predict_test=test1.reshape((len(test1), n_steps, n_features))
print(predict_test)
predictions = model.predict(predict_test)
# round predictions
print(predictions)
    
z=0


for j in predictions:
    if j>0.9:
        z+=1
percent=z/(len(predictions))
print('Percentage of abnormality is',percent*100)


    

    
#rounded = [round(x2[0]) for x2 in predictions]
#print('the results are',rounded)
'''
The following part of program plots the EMG signals
'''
import csv
import numpy
from random import shuffle
import matplotlib.pyplot as plt
patients=['anas.csv','bristo.csv','christy.csv','raees.csv','suresh.csv','abnormal.csv']
s=20
for i in patients:
    data=numpy.loadtxt(i, delimiter=",")
    print('------------------------------------------------------')
    i=i[:-4]
    print('patient name:',i)
    s+=5
    print('age=',s)
    
    plt.plot(data)
    plt.ylabel('EMG Signal')
    plt.show()
