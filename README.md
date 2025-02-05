This is a financial dashboard for a number of different assets: cryptocurrencies, commodities, an ETFs, built using: 

Language: Python
Web Framework: Streamlit 
Data Processing and Analysis: Pandas, Numpy
Financial Data APIs: Yahoo Finance(yfinance), CoinGecko API, Requests
Data Visualisation: Matplotlib
System/OS Operations: OS module

To load the site, open the repo using an IDE and run. 
You should be prompted to run a command in your IDE's terminal that looks like this: 

streamlit run /{file path of app folder}/streamlit_app/streamlit_app.py
  
By running this command, you can open the site that looks like this:

<img width="700" alt="Screenshot 2025-01-22 at 21 49 34" src="https://github.com/user-attachments/assets/66057392-da22-4529-b4b5-e8375178f4e0" />

After navigating away from the sidebar, the landing page looks like this, with a simple chatbot (currently being improved) that can be used to navigate the page. 
The sidebar can also be used to navigate the pages. 

<img width="700" alt="Screenshot 2025-01-22 at 21 49 43" src="https://github.com/user-attachments/assets/e4a81a96-64e0-4693-b6a9-2379ae84acc1" />

After navigating to the "Commodities" page, you are given the option to select as many commdoities as you would like to compare, as well as the period and granularity of the graphs to be produced: 

<img width="400" alt="Screenshot 2025-01-22 at 21 50 18" src="https://github.com/user-attachments/assets/cb6e407f-34fe-45a4-8cad-849697377b54" /> <img width="400" alt="Screenshot 2025-01-22 at 21 54 04" src="https://github.com/user-attachments/assets/d49319b3-40ac-4740-964a-dea4fa273a5c" />

After selecting the commodities you want to compare, the dashboard generates a chart that looks like this: 

<img width="700" alt="Screenshot 2025-01-22 at 21 54 49" src="https://github.com/user-attachments/assets/ea444fd1-e835-4805-ac1b-88c52739dcee" />

When you navigate to the Crypto Dashboard page, you are greeted by a list of the top 200 cryptocurrencies (chosen by largest market cap), includign information such as yesterday's closing price, market cap, current price, and other information: 

<img width="800" alt="Screenshot 2025-01-22 at 21 55 50" src="https://github.com/user-attachments/assets/e167a6a7-b69f-49db-9897-350cd424459c" />







