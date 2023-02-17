import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App #symbolizes header

Shown are the stock closing price and volume of Google!
""")
tickerSymbol = 'GOOGL'
#get data from this ticker 'GOOGLE'
tickerData = yf.Ticker(tickerSymbol)
# get historical prices from this ticker
tickerDf = tickerData.history(period='1d', start = '2010-5-31', end = '2020-5-31')
#open high low close volume divedends stock splits
st.line_chart(tickerDf.close)
st.line_chart(tickerDf.Volume)