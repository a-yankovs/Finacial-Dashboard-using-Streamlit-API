import streamlit as st 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import random 


# Dictionary of top 20 commodities
# Defines the units and names 
commodities_info = {
    "CL=F": {"unit": "barrels", "name": "Crude Oil (WTI)"},
    "BZ=F": {"unit": "barrels", "name": "Brent Crude"},
    "NG=F": {"unit": "mmBtu", "name": "Natural Gas"},
    "HO=F": {"unit": "gallons", "name": "Heating Oil"},
    "RB=F": {"unit": "gallons", "name": "Gasoline (RBOB)"},
    "GC=F": {"unit": "troy ounces", "name": "Gold"},
    "SI=F": {"unit": "troy ounces", "name": "Silver"},
    "HG=F": {"unit": "pounds", "name": "Copper"},
    "PL=F": {"unit": "troy ounces", "name": "Platinum"},
    "PA=F": {"unit": "troy ounces", "name": "Palladium"},
    "ZC=F": {"unit": "bushels", "name": "Corn"},
    "ZS=F": {"unit": "bushels", "name": "Soybeans"},
    "ZW=F": {"unit": "bushels", "name": "Wheat"},
    "ZM=F": {"unit": "tons", "name": "Soybean Meal"},
    "ZL=F": {"unit": "pounds", "name": "Soybean Oil"},
    "ZO=F": {"unit": "bushels", "name": "Oats"},
    "ZR=F": {"unit": "cwt", "name": "Rice"},
    "CT=F": {"unit": "pounds", "name": "Cotton"},
    "KC=F": {"unit": "pounds", "name": "Coffee"},
    "SB=F": {"unit": "pounds", "name": "Sugar"},
    "CC=F": {"unit": "metric tons", "name": "Cocoa"},
    "OJ=F": {"unit": "pounds", "name": "Orange Juice"},
}


@st.cache_data
# acquires data from selected tickers and period
def fetch_commodity_data(tickers, period ="6d", interval = "1d"):
    # try to find exceptions
    try: 
        data = yf.download(tickers, period = period, interval = interval)
        return data
    except Exception as e: 
        st.error("Failed to retrieve commodity data: {str(e)}")
        return pd.DataFrame
    
# streamlit application for the commodities page of the site 
def app(): 
    st.title("Commodities Dashboard")
    st.text("Please select at least one commodity:")
    period = st.selectbox("Select period", ["1D", "5D", "1MO", "3MO", "6MO", "1Y"], index = 3)
    interval = st.selectbox("Select Granularity", ["1D", "5D", "1WK", "1MO"], index = 0)
    selected = st.multiselect("Select Commodities", [commodities_info[ticker]["name"] for ticker in commodities_info], default = [])

    selected_tickers = [ticker for ticker in commodities_info if commodities_info[ticker]["name"] in selected]

    if selected_tickers: 
        data = fetch_commodity_data(selected_tickers, period = period, interval = interval)
        if not data.empty: 
            st.success("Data loaded successfully for selected commodities!")
            dashboard_data = []
            # going through selected commodities, and getting closing prices for last two days
            for commodity in selected:
                commodity_ticker = next(ticker for ticker in commodities_info if commodities_info[ticker]["name"] == commodity)
                commodity_data = data['Close'][commodity_ticker].dropna()
                if len(commodity_data) <= 2:
                    #checking the % change in the last two closure prices for the commodity 
                    last_close = commodity_data.iloc[-1]
                    prev_close = commodity_data.iloc[-2]
                    change = (last_close - prev_close) / prev_close * 100
                    # data displayed on the dashboard: commodity name, ticker, units, last closing price, and % change in price 
                    # stored in the "dashboard_data" list 
                    dashboard_data.append({
                        'Commodity':commodities_info[commodity_ticker]["name"],
                        'Ticker':commodity_ticker, 
                        'Unit': commodities_info[commodity_ticker]["unit"], 
                        'Last closing price': last_close, 
                        'Change': change
                    })
            # converting to pandas dataframe format and transferred to streamlit 
            dashboard_df = pd.DataFrame(dashboard_data)
            st.dataframe(dashboard_df)

            # graphing selected commodities
            plot_price_data(data, selected, selected_tickers)
            
        else: 
            st.warning("No data available for selected commodities")

# plotting commodity price movement
def plot_price_data(data, selected, selected_tickers): 
    fig, ax = plt.subplots(figsize=(10, 5))
    # colors map for the commodities using a random color generator for each commodity 
    colors = {commodity: f"#{random.randint(0, 0xFFFFFF):06x}" for commodity in selected}
    for commodity, ticker in zip(selected, selected_tickers): 
        if ticker in data['Close']: 
            ax.plot(data['Close'][ticker].index, data['Close'][ticker], label = commodity, color = colors[commodity])
    # graph formatting 
    ax.set_title("Commodity Price Comparison")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc = "best")
    st.pyplot(fig)

if __name__ == '__main__': 
    app()