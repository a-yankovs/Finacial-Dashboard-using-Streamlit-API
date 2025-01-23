import streamlit as st
import numpy as np
import time
import random
from pages import commodities, cryptos, etfs_value 
# underpriced_stocks

# site structure 
pages = {
    "Commodities": commodities, 
    "Cryptocurrencies": cryptos, 
    "ETFs": etfs_value, 
    # "Stocks": underpriced_stocks
}

#set up of sidebar navigation in between pages
st.sidebar.title("Site Navigation")
choice = st.sidebar.radio("Choose a page to display", ["Home"] + list(pages.keys()))
if choice != "Home":
    pages[choice].app()
else:
    st.write("# Welcome!")
    st.write("Use the sidebar to navigate between pages.")


# very simple chatbot layout - work in progress 
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "What's up"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages: 
    with st.chat_message(message["role"]): 
        st.markdown(message["content"])

prompt = st.chat_input("How can I help?")
if prompt: 
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): 
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    


     


