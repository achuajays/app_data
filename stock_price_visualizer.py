import streamlit as st
import pandas as pd
import yfinance as yf

st.title('Stock Price Visualizer')

# Input for stock symbol
stock_symbol = st.text_input('Enter stock symbol (e.g., AAPL)', 'AAPL')

# Input for time period
time_period = st.selectbox('Select time period', ['1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])

# Fetch stock data
@st.cache_data
def fetch_stock_data(symbol, period):
    data = yf.download(tickers=symbol, period=period)
    return data

# Display data
def display_data(data):
    st.subheader('Raw Data')
    st.dataframe(data)

# Display line chart for closing prices
def display_chart(data, symbol):
    st.subheader(f'{symbol} Closing Price')
    st.line_chart(data['Close'])

# Main code
if stock_symbol:
    stock_data = fetch_stock_data(stock_symbol, time_period)
    display_data(stock_data)
    display_chart(stock_data, stock_symbol)
import streamlit as st
import pandas as pd
import yfinance as yf

st.title('Stock Price Visualizer')

# Input for stock symbol
stock_symbol = st.text_input('Enter stock symbol (e.g., AAPL)', 'AAPL')

# Input for time period
time_period = st.selectbox('Select time period', ['1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])

# Fetch stock data
@st.cache_data
def fetch_stock_data(symbol, period):
    data = yf.download(tickers=symbol, period=period)
    return data

# Display data
def display_data(data):
    st.subheader('Raw Data')
    st.dataframe(data)

# Display line chart for closing prices
def display_chart(data, symbol):
    st.subheader(f'{symbol} Closing Price')
    st.line_chart(data['Close'])

# Main code
if stock_symbol:
    stock_data = fetch_stock_data(stock_symbol, time_period)
    display_data(stock_data)
    display_chart(stock_data, stock_symbol)
