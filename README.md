# Trend Prediction and High-frequency Trading Strategy Using Limit Order Book

This project explores the application of advanced data processes/machine learning to predict near-term price movements and generate trading signals using Level2 (Limit Order Books) data from financial markets. 

Some of the procedures include time series analysis using ARIMA, SARIMAX and LSTM models for a single tradable asset, regression of price predictions, and classification of buy, sell, and hold signals. A simulated trading environment was used to evaluate the profitability of these models. 

The results from this empirical investigation highlight the challenges and opportunities of leveraging high-frequency trading data in developing automated trading strategies that capitalize on second price movements. The findings emphasize the importance of sophisticated data-processing and feature-engineering techniques to improve the accuracy and profitability of predictive trading models.

# Introduction

## Limit Order Books

<img src="https://github.com/vishal5498/stockPricePrediction/blob/786814cafae60bced617925ba88eaec411f8c43d/Graphical-representation-of-the-Limit-Order-Book.png" width="350">

The LOB shows a live picture of the supply and demand of the securities at any given moment since the limit orders that have not been executed yet live in it. A number of studies have tapped deeper into the LOB to set a ground on the possibility of trend prediction. At the same time, machine learning and deep learning have been widely applied in this field. research has found that with the use of only one feature, the performance of ARIMA significantly surpasses that of LSTM as the time window increases. 

This study attempts to set out on an exploratory journey to address these challenges through classic and advanced modelling methodologies. Initially, the time-series forecasting model ARIMA, is used as the baseline as this model is good at capturing linear correlations. After understanding ARIMA’s limitations in dealing with non-linear nature of LOBs, the investigation proceeded to examine more advanced models such as Seasonal ARIMA with Exogenous Factors (SARIMAX) and Long Short-Term Memory (LSTM) networks.

Beyond price forecasting, the methods employed are further optimized to classify trading actions such as buy, sell, or hold.
