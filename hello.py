""" added getStock(name) method which takes user's stock ticker name and returns a line chart of the open high low close volume
 divedends stock splits if the ticker is valid. App only runs once Enter button is clicked. Testing..."""
import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Hello, welcome to Danny's Stock Price App!

Shown are the stock closing price and volume of Google!
""")
def getStock(name): 
    
 if(name is None):
    return st.write("Error")
 tickerSymbol = name
#get data from user-inputted ticker

 tickerData = yf.Ticker(tickerSymbol)

 info = tickerData.info

 if(info == None):
    return st.write("Error: You inputted invalid ticker, please try again")
 #check to see if ticker is valid

# get historical prices from this ticker
 tickerDf = tickerData.history(period='1d', start = '2023-1-31', end = '2023-2-1')

#open high low close volume divedends stock splits
 st.line_chart(tickerDf.Close)
 st.line_chart(tickerDf.Volume)



name = st.text_input("Enter stock ticker name") #get user input
with st.form(key = 'my_form_submit_button'):
    submit_button = st.form_submit_button(label="Enter")
    if submit_button:
     if name:                                       
      getStock(name) 
     if not name:
      st.write("Error! Empty String")
#C:\Users\Dansa\OneDrive\Desktop>streamlit run hello.py on cmd prompt


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/premium-vector/abstract-trendy-blue-color-gradient-texture-background-website-banner-creative-art-design_120819-388.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
