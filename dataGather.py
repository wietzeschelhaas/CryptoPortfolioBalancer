#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:13:29 2021

@author: wietze
"""


from binance.client import Client



def getColumn(matrix, i):
    return [row[i] for row in matrix]

apiKey = ""

client = Client(apiKey)


klines = client.get_historical_klines("BNBUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Dec, 2017", "25 feb, 2021")
klinesBtc = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Dec, 2017", "25 feb, 2021")
klineseth = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Dec, 2017", "25 feb, 2021")
klinesLtc = client.get_historical_klines("LTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Dec, 2017", "25 feb, 2021")
klinesada = client.get_historical_klines("ADAUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Dec, 2017", "25 feb, 2021")



nClose = getColumn(klinesada,4)

with open('adaOpen', 'w') as f:
    for item in nClose:
        f.write("%s\n" % item)