# displays the top 100 etfs as of 01/22/2025

import streamlit as st
import os
import pandas as pd 
import yfinance as yf 

st.set_page_config(layout = 'wide')

def format_assets(assets): 
    if isinstance (assets, (int, float)): 
        if assets >= 1e9 : 
            return f"{assets/1e9:.3f} B"
        elif assets >= 1e6: 
            return f"{assets/1e6:.3f} M"
    

def fetch_data(symbol): 
    try:
        etf = yf.Ticker(symbol)
        info = etf.info
        return {"Symbol": symbol, "Info": info}
    except Exception as e:
        return {"Symbol": symbol, "Error": str(e)}
    # etf = yf.Ticker(symbol)
    # info = etf.info
    # return {
    #     "Name": info.get("longName", "N/A"), 
    #     "Latest Price": info.get('previousClose', "N/A"), 
    #     "52WK High": info.get('fiftyTwoWeekHigh', "N/A"), 
    #     "52Wk Low": info.get('fifityTwoWeekLow', "N/A"), 
    #     "Total Assets": format_assets(info.get('totalAssets', "N/A")), 
    # }

def app(): 
    st.title("ETF Dashboard")
    file_path = os.path.join(os.path.dirname(__file__), 'etfs.txt') 
    try: 
        with open(file_path, 'r') as file: 
            symbols = [line.strip().upper() for line in file.readlines()]
            data = [fetch_data(symbol) for symbol in symbols]
            # st.write("Fetched Data:", data)
            df = pd.DataFrame(data)
            st.table(df)
    except FileNotFoundError: 
        st.error("ETF Symbol File not found")

if __name__ == '__main__': 
    app()
