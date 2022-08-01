import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader.data import DataReader
from datetime import datetime

start = datetime(2022,3,28)
end = datetime(2022,3,28)
data = DataReader('GDX', 'yahoo', start, end)
data['price'] = data['Adj Close']

SMA = 25
data['SMA'] = data['price'].rolling(window=SMA).mean()

N = 1
data['STD'] = N * data['price'].rolling(window=SMA).std()
data['SMA+STD'] = data['SMA'] + data['STD']
data['SMA-STD'] = data['SMA'] - data['STD']
