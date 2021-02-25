#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:52:12 2021

@author: wietze
"""
import pandas as pd
import matplotlib.pyplot as plt

#Data from 2020-08-01 to 2021-02-25
#bnb = pd.read_csv("/home/wietze/cryptoRebalance/Binance_BNBUSDT_1h.csv").iloc[:,6].head(4964)
#btc = pd.read_csv("/home/wietze/cryptoRebalance/Binance_BTCUSDT_1h.csv").iloc[:,6].head(33548)
#eos = pd.read_csv("/home/wietze/cryptoRebalance/Binance_EOSUSDT_1h.csv").iloc[:,6].head(4964)
#etc = pd.read_csv("/home/wietze/cryptoRebalance/Binance_ETCUSDT_1h.csv").iloc[:,6].head(4964)
#eth = pd.read_csv("/home/wietze/cryptoRebalance/Binance_ETHUSDT_1h.csv").iloc[:,6].head(33548)
#link = pd.read_csv("/home/wietze/cryptoRebalance/Binance_LINKUSDT_1h.csv").iloc[:,6].head(4964)
#ltc = pd.read_csv("/home/wietze/cryptoRebalance/Binance_LTCUSDT_1h.csv").iloc[:,6].head(4964)
#neo = pd.read_csv("/home/wietze/cryptoRebalance/Binance_NEOUSDT_1h.csv").iloc[:,6].head(4964)
#trx = pd.read_csv("/home/wietze/cryptoRebalance/Binance_TRXUSDT_1h.csv").iloc[:,6].head(4964)
#zec = pd.read_csv("/home/wietze/cryptoRebalance/Binance_ZECUSDT_1h.csv").iloc[:,6].head(4964)

with open('bnbOpen') as f:
    bnb = f.read().splitlines()
with open('adaOpen') as f:
    ada = f.read().splitlines()
with open('btcOpen') as f:
    btc = f.read().splitlines()
with open('ethOpen') as f:
    eth = f.read().splitlines()
with open('LtcOpen') as f:
    ltc = f.read().splitlines()


bnb = [float(i) for i in bnb]
ada = [float(i) for i in ada]
btc = [float(i) for i in btc]
eth = [float(i) for i in eth]
ltc = [float(i) for i in ltc]

initialInvest = 10000
portSize = 5

hodlList = []
for x in reversed(range(25002)):
    adaProfit = (ada[x+1] / ada[25002]) * (initialInvest /  portSize)
    ethProfit = (eth[x+1] / eth[25002]) * (initialInvest /  portSize)
    btcProfit = (btc[x+1] / btc[25002]) * (initialInvest /  portSize)
    ltcProfit = (ltc[x+1] / ltc[25002]) * (initialInvest /  portSize)
    bnbProfit = (bnb[x+1] / bnb[25002]) * (initialInvest /  portSize)
    

    #hodlProfit = btcProfit + neoProfit + ltcProfit + ethProfit + bnbProfit + eosProfit + etcProfit + linkProfit + trxProfit +zecProfit
    hodlProfit = btcProfit + ethProfit + ltcProfit + bnbProfit + adaProfit

    hodlList.append(hodlProfit)
####################################################
##########SIMULATE REBALANCE EVERY HOUR#############

totalBalance = initialInvest

reBalanceList =  []

percentList = []
for x in reversed(range(25002)):
    btcProfitSinceLastHour = (btc[x] / btc[x+1]) * (totalBalance /  portSize)
    ethProfitSinceLastHour = (eth[x] / eth[x+1]) * (totalBalance /  portSize)
    ltcProfitSinceLastHour = (ltc[x] / ltc[x+1]) * (totalBalance /  portSize)
    bnbProfitSinceLastHour = (bnb[x] / bnb[x+1]) * (totalBalance /  portSize)
    adaProfitSinceLastHour = (ada[x] / ada[x+1]) * (totalBalance /  portSize)
    
    
    
    
    feeBtc = abs(btc[x] - btc[x+1]) * 0.00075
    feeEth = abs(eth[x] - eth[x+1]) * 0.00075
    

    totalBalance = btcProfitSinceLastHour + ethProfitSinceLastHour + bnbProfitSinceLastHour + ltcProfitSinceLastHour + adaProfitSinceLastHour  - feeBtc - feeEth
    #totalBalance = eosProfitSinceLastHour + zecProfitSinceLastHour + trxProfitSinceLastHour+  linkProfitSinceLastHour + etcProfitSinceLastHour + bnbProfitSinceLastHour+ btcProfitSinceLastHour + ethProfitSinceLastHour + neoProfitSinceLastHour + ltcProfitSinceLastHour
    
    reBalanceList.append(totalBalance)
    




import matplotlib.pyplot as plt




plt.plot(hodlList, label = "hodl")
plt.plot(reBalanceList, label = "rebalance")



# Set a title of the current axes.
plt.title('Rebalance vs hodl')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()

