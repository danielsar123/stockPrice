""" added getStock(name) method which takes user's stock ticker name and returns a line chart of the open high low close volume
 divedends stock splits if the ticker is valid. App only runs once Enter button is clicked. """
import yfinance as yf
import streamlit as st
import pandas as pd
import datetime as dt

st.write("""
# Hello, welcome to Danny's Stock Price App!

Shown are the stock closing price and volume of whatever you choose!
""")
def getStock(name,startD,endD): 
    
 if(name is None):
    return st.write("Error")
 if(startD>endD or startD == endD):
    return st.write("Error! wrong date")
 tickerSymbol = name
 
#get data from user-inputted ticker

 tickerData = yf.Ticker(tickerSymbol)
 #check to see if ticker is valid

# get historical prices from this ticker
 tickerDf = tickerData.history(period='1d', start = startD, end = endD)
 if(tickerDf.Close.empty):
    return st.write("Error! Invalid Stock Ticker") ##.info method stopped working (yfinance side error) had to handle error other way
#open high low close volume divedends stock splits
 st.line_chart(tickerDf.Close)
 st.line_chart(tickerDf.Volume)



with st.form(key = 'my_form_submit_button'):
    startD = st.date_input("Input start date")
    endD = st.date_input("Input end date")  
    name = st.text_input("ticker goes here") #get user input
    submit_button = st.form_submit_button(label="Enter")
    if submit_button:
     if name:                                       
      getStock(name,startD,endD) 
     if not name:
      st.write("Error! Empty String")
#C:\Users\Dansa\OneDrive\Desktop>streamlit run hello.py on cmd prompt



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/jpeg;base64,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");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


