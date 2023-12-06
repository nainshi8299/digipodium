import math
import numpy as np
import pandas as pd
from datetime import date, timedelta
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.preprocessing import minmax_scale
from sklearn.metrics import mean_absolute_error,mean_squared_error
from keras.models import Sequential
from keras.layers import LSTM ,Dense



today=date.today()
date_today=today.strftime("%Y-%m-%d")
date_start='2019/01/01'



#get stock
Stock=input("enter stock name:")
stockname=Stock
symbol= '</>'

from pandas_datareader import data as webreader
df=webreader.datareader(symbol,start=date_start,end=date_today,data_source="yahoo")

import yfinance as yf
df=yf.download(symbol,start=date_start,end=date_today)

print(df.shape)
df.head(5)

register_matplotlib_converters()
years=mdates.YearLocator()
fig,ax1=plt.subplots(figsize=(16,6))
ax1.xaxis.set_major_locator(years)
x= df.index
y= df['close']
ax1.fill_between(x,0,y,color='#b9e1fa')
ax1.legend([stockname],fontsize=12)