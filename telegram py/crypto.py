import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


# titles and descriptions
st.title("Cryptocurrency Analysis")

st.header("Project looking at cryptocurrency trends over time")

st.image("https://img.freepik.com/free-photo/3d-rendering-bitcoin-other-crypto-currencies-led-glow-dark-glossy-glass-board-with-blockchain-data-dots-lines_163855-4.jpg?size=626&ext=jpg")


# sidebar
st.sidebar.title("Options")

st.sidebar.header("Cryptocurrency Symbols")

option = st.sidebar.selectbox("Select from the following cryptocurrencies:", ('AAVE', 'BNB', 'BTC', 'ADA', 'LINK', 'ATOM', 'CRO', 'DOGE', 'EOS', 'ETH', 'MIOTA', 'LTC', 'XMR', 'XEM', 'DOT', 'SOL', 'XLM', 'USDT', 'TRX', 'UNI', 'USDC', 'WBTC', 'XRP'))

# displaying the data
st.header(option)

'''
Dataset holds the following:

Name, Symbol, Date, High, Low, Opening Price, Closing Price
* Name/Symbol = Cryptocurrency
* Date = Observation date
* High = The highest price that day
* Low = The lowest price that day
* Open = The opening price that day
* Close = The closing price that day
* Volume = Volume of transactions that day
* Market Cap = Market capitalization in USD

[Link] (https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory) to the source of the dataset (Cryptocurrency Historical Prices).
'''

# crypto dictionary
if option == 'AAVE':
    filename = 'Aave'
elif option == 'BNB':
    filename = 'BinanceCoin'
elif option == 'BTC':
    filename = 'Bitcoin'
elif option == 'ADA':
    filename = 'Cardano'
elif option == 'LINK':
    filename = 'ChainLink'
elif option == 'ATOM':
    filename = 'Cosmos'
elif option == 'CRO':
    filename = 'CryptocomCoin'
elif option == 'DOGE':
    filename = 'Dogecoin'
elif option == 'EOS':
    filename = 'EOS'
elif option == 'ETH':
    filename = 'Ethereum'
elif option == 'MIOTA':
    filename = 'Iota'
elif option == 'LTC':
    filename = 'Litecoin'
elif option == 'XMR':
    filename = 'Monero'
elif option == 'XEM':
    filename = 'NEM'
elif option == 'DOT':
    filename = 'Polkadot'
elif option == 'SOL':
    filename = 'Solana'
elif option == 'XLM':
    filename = 'Stellar'
elif option == 'USDT':
    filename = 'Tether'
elif option == 'TRX':
    filename = 'Tron'
elif option == 'UNI':
    filename = 'Uniswap'
elif option == 'USDC':
    filename = 'USDCoin'
elif option == 'WBTC':
    filename = 'WrappedBitcoin'
elif option == 'XRP':
    filename = 'XRP'


# loading the dataframe
df = pd.read_csv(f"C:/Users/richa/Documents/Coding+/SPR21/csce 5300 (big data)/telegram py/crypto_data/coin_{filename}.csv")

st.dataframe(df)



# sidebar options logic
st.header(option)

st.subheader("Classic Candlestick Chart for Financial Analysis")

st.write("Note: A Candlestick Chart has similar features to a boxplot. However, the bottom and top whiskers denote "
         "the Low and High for each day, respectively. The green color indicates a 'Bullish Candle Stick' where the "
         "Closing price was greater than the Opening price; red indicates a 'Bearish Candle Stick' where the Opening "
         "was greater than the Closing.")

# plotly candlestick graph
candlestick = go.Candlestick(x=df['Date'],
               open=df['Open'],
               high=df['High'],
               low=df['Low'],
               close=df['Close']
               )

figure = go.Figure(data=[candlestick])

figure.update_layout(
    title={
        'text': f"{option} Candlestick Graph",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
        },
    xaxis_title="Date",
    yaxis_title="Price"
)

st.plotly_chart(figure)