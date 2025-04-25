import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
import matplotlib.pyplot as plt

def search(stockName):
    try:
        Image = open('static/stocks/'+stockName+'/'+stockName+'1.png', 'r')
        # Store configuration file values
        print("cache found")
        return 1

    except FileNotFoundError:
        # Keep preset values
        print("file not found")
        return 0

#Function to process the data into 7 day look back slices
def processData(data,lb):
    X,Y = [],[]
    for i in range(len(data)-lb-1):
        X.append(data[i:(i+lb),0])
        Y.append(data[(i+lb),0])
    return np.array(X),np.array(Y)
