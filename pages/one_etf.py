import json

# The raw ETF data as a Python dictionary
etf_info = {
    "ask": 28.76,
    "askSize": 100,
    "averageDailyVolume10Day": 67573960,
    "averageVolume": 76102560,
    "averageVolume10days": 67573960,
    "bid": 28.6,
    "bidSize": 100,
    "category": "Trading--Leveraged Equity",
    "currency": "USD",
    "dayHigh": 30.08,
    "dayLow": 28.4232,
    "exchange": "NGM",
    "fiftyDayAverage": 26.1018,
    "fiftyTwoWeekHigh": 41.5,
    "fiftyTwoWeekLow": 4.94,
    "firstTradeDateEpochUtc": 1660051800,
    "fundFamily": "Direxion Funds",
    "fundInceptionDate": 1659916800,
    "gmtOffSetMilliseconds": -18000000,
    "legalType": "Exchange Traded Fund",
    "longBusinessSummary": "The fund, under normal circumstances, invests at least 80% of its net assets (plus any borrowings for investment purposes) in the securities of TSLA and financial instruments, such as swap agreements and options, that provide leveraged exposure to TSLA. The fund is non-diversified.",
    "longName": "Direxion Daily TSLA Bull 2X Shares",
    "maxAge": 86400,
    "messageBoardId": "finmb_1793225454",
    "navPrice": 29.547,
    "open": 28.54,
    "phone": "866-476-7523",
    "previousClose": 29.53,
    "priceHint": 2,
    "quoteType": "ETF",
    "regularMarketDayHigh": 30.08,
    "regularMarketDayLow": 28.4232,
    "regularMarketOpen": 28.54,
    "regularMarketPreviousClose": 29.53,
    "regularMarketVolume": 36932161,
    "shortName": "Direxion Daily TSLA Bull 2X Sha",
    "symbol": "TSLL",
    "timeZoneFullName": "America/New_York",
    "timeZoneShortName": "EST",
    "totalAssets": 4806493696,
    "trailingPE": 58.30122,
    "twoHundredDayAverage": 13.89075,
    "underlyingSymbol": "TSLL",
    "uuid": "03513f8c-ef65-3691-9289-fd3e6a3b94ee",
    "volume": 36932161,
    "yield": 0.0137,
    "ytdReturn": 0.072648
}

# Convert to the desired format
formatted_output = ", ".join([f"{key}: {value}" for key, value in etf_info.items()])

# Print the result
print(formatted_output)
