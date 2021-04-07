import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


# titles and descriptions
st.title("Telegram Cryptocurrency Analysis")

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

### riyad's code ###
st.header('Past 3 Months Analysis')
st.subheader('Data and Analyses from 1/28/21 to 3/23/21')

@st.cache
def load_binance():
	col_names = ['id','date','from','from_id','text']
	data = pd.read_csv('binance.csv', names=col_names)
	data = data.iloc[1:]
	return data
@st.cache
def load_bittrex():
	col_names = ['id','date','from','from_id','reply_to_message_id','text']
	data = pd.read_csv('bittrex.csv', names=col_names)
	data = data.iloc[1:]
	return data
@st.cache
def load_huobi():
	col_names = ['id','date','from','from_id','text']
	data = pd.read_csv('huobi.csv', names=col_names)
	data = data.iloc[1:]
	return data
@st.cache
def load_kucoin():
	col_names = ['id','date','from','from_id','text']
	data = pd.read_csv('kucoin.csv', names=col_names)
	data = data.iloc[1:]
	return data
@st.cache
def load_OKEx():
	col_names = ['id','date','from','from_id','reply_to_message_id','text']
	data = pd.read_csv('OKEx.csv', names=col_names)
	data = data.iloc[1:]
	return data


show_data = st.selectbox("Show Sample Data", ["Please select", "Binance", "Bittrex", "Huobi", "Kucoin", "OKEx"])
if show_data == "Binance":
	df1 = load_binance()
	st.subheader('Binance data')
	st.write(df1.head(10))
elif show_data == "Bittrex":
	df2 = load_bittrex()
	df2 = df2.drop('reply_to_message_id', 1)
	st.subheader('Bittrex data')
	st.write(df2.head(10))
if show_data == "Huobi":
	df3 = load_huobi()
	st.subheader('Huobi data')
	st.write(df3.head(10))
if show_data == "Kucoin":
	df4 = load_kucoin()
	st.subheader('Kucoin data')
	st.write(df4.head(10))
if show_data == "OKEx":
	df5 = load_OKEx()
	df5 = df5.drop('reply_to_message_id', 1)
	st.subheader('OKEx data')
	st.write(df5.head(10))


trend = st.selectbox("Telegram Discussion Trends", ["Please select", "Bitcoin vs Ether", "DOT vs XRP vs LTC vs XLM",
	"Bitcoin vs DeFi", "Centralized stablecoins (USDT) vs decentralized (DAI)",
	"Decentralized exchanges (UNISWAP vs Sushiswap vs 1inch)", "DeFi protocols (MakerDAO vs Compound)"])

@st.cache
def load_crypto():
	df = pd.read_csv('crypto.csv')
	return df

crypto = load_crypto()

if trend == "Bitcoin vs Ether":
	fig = px.scatter(crypto,
                x='date',
                y=['btc','eth'],
                hover_name='date',
                title="Telegram Discussions: BTC vs ETH")
	st.plotly_chart(fig)
elif trend == "DOT vs XRP vs LTC vs XLM":
	fig = px.scatter(crypto,
                x='date',
                y=['dot','xrp','ltc','xlm'],
                hover_name='date',
                title="Telegram Discussions: DOT vs XRP vs LTC vs XLM")
	st.plotly_chart(fig)
elif trend == "Bitcoin vs DeFi":
	fig = px.scatter(crypto,
                x='date',
                y=['btc','defi'],
                hover_name='date',
                title="Telegram Discussions: BTC vs DeFi")
	st.plotly_chart(fig)
elif trend == "Centralized stablecoins (USDT) vs decentralized (DAI)":
	fig = px.scatter(crypto,
                x='date',
                y=['usdt','dai'],
                hover_name='date',
                title="Stable coins: USDT vs DAI")
	st.plotly_chart(fig)
elif trend == "Decentralized exchanges (UNISWAP vs Sushiswap vs 1inch)":
	fig = px.scatter(crypto,
                x='date',
                y=['uniswap','sushiswap','1inch'],
                hover_name='date',
                title="DEX: UNISWAP vs Sushiswap vs 1inch")
	st.plotly_chart(fig)
elif trend == "DeFi protocols (MakerDAO vs Compound)":
	fig = px.scatter(crypto,
                x='date',
                y=['makerdao','compound'],
                hover_name='date',
                title="DeFi protocols (MakerDAO vs Compound)")
	st.plotly_chart(fig)

### end of riyad's code ###

### araib's analysis ###
st.subheader('More Analyses from 1/28/21 to 3/23/21')
'''
[Link] (https://github.com/PoliNemkova/Telegram_analysis/tree/streamlit/images_from_others) to source of the data analyses.
'''

st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/araib/3mo_BTCvsDeFi.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/araib/3mo_BTCvsETH.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/araib/3mo_DEX.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/araib/3mo_DOT_XRP_LTC_XLM.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/araib/3mo_MakerDaovsCompound.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/araib/3mo_USDTvsDAI.PNG")

### poli's analysis ###
st.subheader('Prices vs Mentions in Telegram, 1/28/21 to 3/23/21')

st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/poli/btc.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/poli/etc.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/poli/ltc.PNG")

### wesley's analysis ###
st.subheader('Crypto Sentiment Analysis, 1/28/21 to 3/23/21')

st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/wesley/SA_1inch.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/wesley/SA_btc.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/wesley/SA_compound.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/wesley/SA_dai.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/wesley/SA_defi.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/wesley/SA_makerdao.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/wesley/SA_sushiswap.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/wesley/SA_uniswap.PNG")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/wesley/SA_usdt.PNG")

### previous 3 years ###
st.header('Past 3 Years')
st.subheader('Data Analyses from 2018 till Jan 2021')

st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/3_yrs/3yrs_btc_defi.png")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/3_yrs/3yrs_btc_eth.png")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/3_yrs/3yrs_dexs.png")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/3_yrs/3yrs_dot_xrp_ltc_xlm.png")
st.image("https://raw.githubusercontent.com/PoliNemkova/Telegram_analysis/streamlit/images_from_others/3_yrs/3yrs_usdt_dai.png")