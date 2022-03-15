# HW: Python Finance Info - Individual Homework
from symtable import Symbol
import yfinance as yf
import datetime
 
# Description
# The goal of this lab is to practice the usage of Python with networking programming. Perform the following:
# Setup your Python development environment
# Research to find a set of python API that you can use to retrieve financial data. (Hint: Google, Yahoo, etc.)
# Using Yahoo Finance python module for API

# stock = yf.Ticker("ADBE")
# # get stock info
# print(stock.info)
# # get historical market data
# hist = stock.history(period="5d")

while(1):
    print("Input: ")
    # Current date and time
    current = datetime.datetime.now()
    time_to_string = current.strftime("%c")

    # Implement a Python program where it will take a stock symbol as input and output the following:
    # Full name of the company
    print("Please enter a symbol:")
    s_name = input()
    
    # Your program must handle any error situation (such as no network, invalid symbol, etc.)
    try:
        stock = yf.Ticker(s_name)
    except ConnectionError as e:
        print("Connection error", e)
        break
    
    if(stock.info['regularMarketPrice'] is None):
        # Invalid Symbol
        print("Enter another symbol")
    else:
        print("Output: ")
        print(time_to_string)
        print(stock.info['longName'],"(",s_name,")")

    # Stock price
    current_price = stock.info['currentPrice']
    closing_price = stock.info['previousClose']
    # Value changes (+ for increase and - for decrease)
    price_diff = current_price - closing_price
    # Percentage changes (+ for increase and - for decrease)
    percent_diff = (abs(current_price - closing_price)/closing_price)*100
    if(price_diff > 0):
        print(current_price,"+",price_diff,"(+",percent_diff, "%)")
    else:
        print(current_price,"-",abs(price_diff),"(-",percent_diff, "%)")