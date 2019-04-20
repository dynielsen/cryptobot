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


api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']

client = Client(api_key, api_secret)



#%%
def get_volumes():
    #%%
    import pandas as pd
    data=client.get_products()
    data2=data['data']
#    data3=data2[0]
#    data4=data3['volume']
#    print(data4)
#    print(data3['symbol'])
    
    df=pd.DataFrame(data2)
    tradedMoney=df['volume']
    symbol=df['symbol']
    
    newdata=[tradedMoney, symbol]
#    df2=pd.concat(tradedMoney, symbol)
    df3=tradedMoney.to_frame().join(symbol)
    
    
    df3_sorted=df3.sort_values('volume')
    df3_sorted2=df3_sorted.reset_index()
    
    last=len(df3_sorted2)-1
    
    highest_volume_symbol=df3_sorted2.loc[last,'symbol']
    
    top_ten_highest_volume_symbol=list(df3_sorted2.loc[last-10:last,'symbol'])
#    print(top_ten_highest_volume_symbol)
    #%%
    return top_ten_highest_volume_symbol


#%%
def get_volumes2(dataframe):
    #%%
    
    df=dataframe
    tradedMoney=df['tradedMoney']
    symbol=df['symbol']
    
    newdata=[tradedMoney, symbol]
#    df2=pd.concat(tradedMoney, symbol)
    df3=tradedMoney.to_frame().join(symbol)
    
    
    df3_sorted=df3.sort_values('tradedMoney')
    df3_sorted2=df3_sorted.reset_index()
    
    last=len(df3_sorted2)-1
    
    highest_volume_symbol=df3_sorted2.loc[last,'symbol']
    
    top_ten_highest_volume_symbol=list(df3_sorted2.loc[last-10:last,'symbol'])
#    print(top_ten_highest_volume_symbol)
    #%%
    return top_ten_highest_volume_symbol


def get_pairs(market):
   #%%
#    baseAsset='BTC'
    import pandas as pd
    data=client.get_products()
    data2=data['data']
#    data3=data2[0]
#    data4=data3['volume']
#    print(data4)
#    print(data3['symbol'])
    
    df=pd.DataFrame(data2)
    df2=df.loc[df['market'] == market]
    df2=df2.reset_index()
    
    return df2

    
    #%%
    tradedMoney=df['volume']
    symbol=df['symbol']
    
    newdata=[tradedMoney, symbol]
#    df2=pd.concat(tradedMoney, symbol)
    df3=tradedMoney.to_frame().join(symbol)
    
    
    df3_sorted=df3.sort_values('volume')
    df3_sorted2=df3_sorted.reset_index()
    
    last=len(df3_sorted2)-1
    
    highest_volume_symbol=df3_sorted2.loc[last,'symbol']
    
    top_ten_highest_volume_symbol=list(df3_sorted2.loc[last-10:last,'symbol'])
#    print(top_ten_highest_volume_symbol)
    #%%
    return top_ten_highest_volume_symbol


