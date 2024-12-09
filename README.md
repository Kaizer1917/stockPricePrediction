# Trend Prediction and High-frequency Trading Strategy Using Limit Order Book

This project explores the application of advanced data processes/machine learning to predict near-term price movements and generate trading signals using Level2 (Limit Order Books) data from financial markets. 

Some of the procedures include time series analysis using ARIMA, SARIMAX and LSTM models for a single tradable asset, regression of price predictions, and classification of buy, sell, and hold signals. A simulated trading environment was used to evaluate the profitability of these models. 

The results from this empirical investigation highlight the challenges and opportunities of leveraging high-frequency trading data in developing automated trading strategies that capitalize on second price movements. The findings emphasize the importance of sophisticated data-processing and feature-engineering techniques to improve the accuracy and profitability of predictive trading models.

## Introduction

### Limit Order Books

<img src="https://github.com/vishal5498/stockPricePrediction/blob/786814cafae60bced617925ba88eaec411f8c43d/Graphical-representation-of-the-Limit-Order-Book.png" width="350">

The Limit Order Books (LOB) shows a live picture of the supply and demand of the securities at any given moment since the limit orders that have not been executed yet live in it. A number of studies have tapped deeper into the LOB to set a ground on the possibility of trend prediction. At the same time, machine learning and deep learning have been widely applied in this field. Research has found that with the use of only one feature, the performance of autoregressive integrated moving average (ARIMA) significantly surpasses that of long-short term memory (LSTM) as the time window increases. 

This study attempts to set out on an exploratory journey to address these challenges through classic and advanced modelling methodologies. Initially, the time-series forecasting model ARIMA, is used as the baseline as this model is good at capturing linear correlations. After understanding ARIMA’s limitations in dealing with non-linear nature of LOBs, the investigation proceeded to examine more advanced models such as Seasonal ARIMA with Exogenous Factors (SARIMAX) and Long Short-Term Memory (LSTM) networks.

Beyond price forecasting, the methods employed are further optimized to classify trading actions such as buy, sell, or hold.

### Exploratory Data Analysis

In the development of our data-driven model, an essential step was the extraction and cleaning of features from the LOBs. A structured approach was devised to parse and extract relevant features from each line of the raw data files,specifically focusing on bid and ask prices. Subsequent to this basic outlier management, further cleaning was heavily reliant on the aggregation of data into time windows. 

To understand the distribution of the numerical features, density plots, basic statistical descriptors like mean, median, and standard deviation are generated for key variables such as Average Price. 

<img src="https://github.com/vishal5498/stockPricePrediction/blob/ed66a27096ba324d3f663226123eef4f64d52606/Density%20Graph.png" width = "200"> <img src="https://github.com/vishal5498/stockPricePrediction/blob/ed66a27096ba324d3f663226123eef4f64d52606/Density%20Graph.png" width = "200">

We further explore relationships among variables through correlation analyses, employing both Pearson and Spearman methods to measure linear and rank correlations, respectively. These relationships are visualized using heatmaps, which provide intuitive graphical representations of the correlation coefficients, enhancing the understanding of interdependencies among the features.

<img src="https://github.com/vishal5498/stockPricePrediction/blob/ed66a27096ba324d3f663226123eef4f64d52606/Spearman_Correlation_martix.png" width=400>

Notably, a very high correlation (near 1.0) is observed between max bid and avg price, and similarly between min ask and avg price, indicating that these max bid and min ask prices are strong predictors of the average price. Conversely, ask level diff shows a notably strong negative correlation with both max bid and avg price (approximately -0.81), highlighting an inverse relationship with increasing bid levels leading to decreasing ask level differences.

## Modelling

### ARIMA

Due to the vast amount of data, we initially used a smaller dataset to quickly verify the method. The training data originate from cleaned LOB (Limit Order Book) data. Since ARIMA works with univariate input data, we select the next k average price change(lt) calculated from the LOB for our analysis. We start the experiment with 500 data points and find that the curve of the forecasted results from the ARIMA model significantly deviates from the actual value curve, indicating that the model fails to effectively learn the dynamic changes within the data. Therefore, we attempt to increase the data volume to 5,000, and the results are shown in Fig. 5. We observe that there is almost no improvement in the curve fitting. 

### SARIMA

In implementing the SARIMAX model, this project uses the following features, max bid, min ask, avg price, bid level diff, ask level diff, bid cumulative depth, ask cumulative depth, as exogenous variables to assist in predicting the target variable lt. (k=10)
