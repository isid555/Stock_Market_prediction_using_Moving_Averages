import numpy as np 
import pandas as pd 
import matplotlib.pyplot as  plt 
import pandas_datareader as data 
import yfinance as yf 
import streamlit as st
from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')
print(current_date)

start ='2013-05-05'
end = current_date


st.title("Stock Market Prediction using Moving Averages")
user_input = st.text_input("Enter Stock Ticker","^NSEI")
df = yf.download(user_input, start=start, end=end)
st.subheader("Data from 2013")
st.write(df.describe())
#Visuals
st.subheader('There you go!')
ma100  = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(15,9))
plt.plot(df.Close)
plt.plot(ma100, 'r')
plt.plot(ma200 , 'g')
plt.title("Stock Prediction using Moving Averages")
plt.xlabel("Time")
plt.ylabel("Price")
# plt.legend()
# plt.show()
st.pyplot(fig)



