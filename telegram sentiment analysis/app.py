import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
st.title("Telegram Sentiment Analysis")
st.write("There are multiple cryptocurrency channels in Telegram that appear to have an effect on the price of some coins. \
In this project we aim to identify curious patterns of bitcoins over the timeline.")


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

# SIDEBAR
st.sidebar.header("About")
