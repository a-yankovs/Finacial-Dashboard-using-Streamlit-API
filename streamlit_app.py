import streamlit as st
from pages import commodities, cryptos, etfs_value, underpriced_stocks

# site structure 
pages = {
    "Commodities": commodities, 
    "Cryptocurrencies": cryptos, 
    "ETFs": etfs_value, 
    "Stocks": underpriced_stocks
}

#set up of sidebar navigation in between pages
st.sidebar.title("Site Navigation")
choice = st.sidebar.radio("Choose a page to display", ["Home"] + list(pages.keys()))
if choice != "Home":
    pages[choice].app()
else:
    st.write("# Welcome!")
    st.write("Use the sidebar to navigate between pages.")


