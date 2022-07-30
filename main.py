# so today we are gonna create a simple stock price app
# these are the data science mini projects
# You can customise it as per your needs
#so lets begin

#import all the packages or if u dont hv install it by type the
#command pip install streamlit yfinance pandas
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("Simple Stock Price App")
tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id', start='2010-01-01', end='2020-07-20')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)