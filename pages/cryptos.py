# A streamlit dashboard for crypto currencies using the coingecko API 

import streamlit as st
import pandas as pd 
import requests 

# method which fetches crypto data from coingecko 
# uses the 'parameters' dictionary to fetech relevant data
def fetch_crypto_data(): 
    url = "https://api.coingecko.com/api/v3/coins/markets"
    parameters = {
        'vs_currency' : 'usd', 
        'order' : 'market_cap_desc', 
        'per_page': 500, 
        'page': 1, 
        'sparkline': False, 
        'price_change_percentage': '24h, 7d'
    }

    # receives response and converts to json format
    response = requests.get(url, params = parameters)
    
    if response.status_code == 200: 
        return response.json()
    else: 
        (f"Failed to fetch data: {response.status_code}")
        return[]
    

def prepare_data(data): 
    cryptos = []
    for item in data: 
        symbol = item.get('symbol', ' ').upper()
        name = item.get('name', 'N/A')
        current_price = item.get('current_price', 'N/A')
        price_change_24h = item.get('price_change_percentage_24h', 'N/A')
        market_cap = item.get('market_cap', 'N/A')
        if isinstance(current_price, (int, float)) and isinstance(price_change_24h, (int, float)):
            prev_price = (current_price/(1 + price_change_24h/100))
        else: 
            prev_price = 'N/A'

        cryptos.append({
            "Symbol": symbol, 
            "Name": name, 
            "Current Price ": current_price, 
            "Previous day price": prev_price, 
            "24H Change": price_change_24h, 
            "Market Cap": market_cap
        })

    return pd.DataFrame(cryptos)

# Fucntion which creates streamlit application 
def app(): 
    st.title(" 📈 Crypto Dashboard ")
    with st.spinner("Fetching Crypto Data..."):
        data = fetch_crypto_data()
        # st.write("Fetched Data:", data)
        df = prepare_data(data)
        df.index += 1
    
    st.dataframe(
         # lambda function which is applied to each value of the 24H change 
        # if the 24h change is more than 25, the function colors the cell green 
        df.style.apply( 
            lambda x: [
                'background-color: #228B22' if isinstance(v, (int, float)) and v >= 25 else '' 
                if isinstance(v, (int, float)) else ''
                for v in x
            ], 
            subset = ['24H Change']
        )
    )

if __name__ == '__main__': 
    app()






