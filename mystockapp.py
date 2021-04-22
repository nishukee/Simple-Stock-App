# A Simple Stock App based on the one shown in the linked article below
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

import yfinance as yf 
import streamlit as st 

st.header('Simple Stock App')

tickers = {'Google': 'GOOGL','Microsoft': 'MSFT','Apple': 'AAPL','Tesla': 'TSLA','Amazon': 'AMZN','Samsung': 'SSNLF','AMD': 'AMD','Intel': 'INTC','Nvidia': 'NVDA','Sony': 'SNE','IBM': 'IDM','HP': 'HPQ','Panasonic': 'PCRFY','Facebook': 'FB'}

options = st.selectbox('Select Company',('Google','Microsoft','Apple','Tesla','Amazon','Samsung','AMD','Intel','Nvidia','Sony','IBM','HP','Panasonic','Facebook'))

st.write('Shown are the stock ***closing price*** and ***volume*** of '+options)

ticketSymbol = tickers[options]

tickerData = yf.Ticker(ticketSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High     Low     Close   Volume  Dividends       Stock Splits

st.subheader('Closing Price')
st.line_chart(tickerDf.Close)

st.subheader('Volume Price')
st.line_chart(tickerDf.Volume)