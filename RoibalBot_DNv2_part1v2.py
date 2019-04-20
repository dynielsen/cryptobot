"""
The Purpose of the RoibalBot Python Program is to create an automated trading bot (functionality) on Binance
Utilized Python-Binance ( https://github.com/sammchardy/python-binance )
Advanced-Version capable of all exchanges, all coins (using cctx)
Created 4/14/2018 by Joaquin Roibal
V 0.01 - Updated 4/20/2018
v 0.02 - Updated 5/30/2018 - Converted to Advanced Version: https://github.com/Roibal/Cryptocurrency-Trading-Bots-Python-Beginner-Advance
Licensed under MIT License
Instructional Youtube Video: https://www.youtube.com/watch?v=8AAN03M8QhA
Did you enjoy the functionality of this bot? Tips always appreciated.
BTC:
ETH:
NOTE: All Subsequent Version of Program must contain this message, unmodified, in it's entirety
Copyright (c) 2018 by Joaquin Roibal
"""

from binance.client import Client
import time
import matplotlib
import os
from matplotlib import cm
import matplotlib.pyplot as plt
from binance.enums import *
import save_historical_data_Roibal_DNv3
from BinanceKeys import BinanceKey1
from various_functions import *
#%%
api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']

client = Client(api_key, api_secret)

# get a deposit address for BTC
address = client.get_deposit_address(asset='BTC')


    # get system status
    #Create List of Crypto Pairs to Watch
list_of_symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT','BNBBTC', 'ETHBTC', 'LTCBTC']
top10=get_volumes()
micro_cap_coins = ['ICXBNB', 'BRDBNB', 'NAVBNB', 'RCNBNB']
#time_horizon = "Short"


#        os.mkdir("Results")
os.chdir("/Users/Daniel/Documents/cryptobot/work/roibalv2/Resultsv2")
#Example Visualizations of Coins

#Visualize All Micro Cap Coins for 8 hour period and 3 minute Candlestick
for coin in top10:
    save_historical_data_Roibal_DNv3.save_historic_klines_csv(coin, "1 hours ago UTC", "now UTC", Client.KLINE_INTERVAL_1MINUTE)



#%%


#%%    
df=get_pairs('BTC')
top_ten_highest_volume_symbol=get_volumes2(df)