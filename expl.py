# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:01:38 2024
@author: Vishal Chavan
"""
import pandas as pd
import json
config = json.load(open("config.json"))
lob = []
import ast
bids = []
time = []
n = []
m_price=[]
number_of_prices = 10
asks = []
time = []
n = []
m_price = []
df['Duration'] = df['time'].astype(float).diff(1)
df['maxbid_diff'] = df['max_bid'].astype(int).diff()
df['minask_diff'] = df['min_ask'].astype(int).diff()
df['marketprice_diff'] = df['market_price'].astype(float).diff()
df['bid_cumulative_depth'] = df['bid_price'].apply(lambda x: sum([i[1] for i in x]) if x else None)
df['ask_cumulative_depth'] = df['ask_price'].apply(lambda x: sum([i[1] for i in x]) if x else None)
df['bid_ask_depth_diff'] = df['bid_cumulative_depth'] - df['ask_cumulative_depth']