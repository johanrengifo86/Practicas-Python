import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
plt.style.use("seaborn")

df = pd.read_csv("eurusd.csv", parse_dates = ["Date"], index_col = "Date")
df
