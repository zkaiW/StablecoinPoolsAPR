# Introduction
This project attempts to see if it is possible to use analytics to consistently forecast APR in Stablecoin liquidity pools .

## Background

Yield farming is the process of providing liquidity to DeFi protocols such as liquidity pools and borrowing and lending services. We are primarily interested in liquidity pools. 

Providing liquidity to liquidity has the potential to yield lucrative returns through high interest rates. However, this is often extremely volatile and unpredictable. 

We attempted to find out if we were able to use traditional analytics techniques to more accurately predict which pools we would be wiser to invest in. 



## Process

### Obtain dataset

In order to perform analysis, we first needed to obtain historical data of DAPR of liquidity pools. We managed to find a site (https://yieldsamurai.com) that compiles and hosts historical data of various pools within various protocols. 

To scrape it, we first attempted to use BeautifulSoup and Selenium. However, we were not successful. We realised that we could use Python's Request library to make web requests. We thus obtained the csv files of the liquidity pools data we were interested to analyse.

<img width="332" alt="DAPR:Time CSV SS" src="https://user-images.githubusercontent.com/76109881/206407881-d09348fe-d6f4-4f99-a96e-019c69213318.png">


### Analysis

Since we are attempting to forecast future DAPR values using past DAPR data, we decided that the most ideal algorithm to be used would be a time series algorithm.  

Our project is only interested in DAPR values against time, hence we are dealing with a univariate time series.

#### ARIMA
The first model we decided to attempt was ARIMA, a classical time series model. We made sure to use a rolling forecast to ensure our model predicts only one time period ahead, to increase accuracy. After developing the model, we realised that the accuracy was not good enough for us to make proper predictions based on this model.

![ARIMA DAPR Forecast plot](https://user-images.githubusercontent.com/76109881/206407896-702d5b3a-b834-4d26-af36-5179de37c7cb.png)

#### LSTM
The next model we decided to use was LSTM, a Recurrent Neural Network. We deduced that since ARIMA, a classical time series model provided less than ideal results, we could explore the possibility of using RNNs, which take into account not just the current data, but the data from the previous time frame to calculate future results, which is applicable to our time series analysis. Whilst LSTM provided significantly better results than ARIMA, we were still unsatisfied with the accuracy of the results.
![LSTM DAPR Forecast plot](https://user-images.githubusercontent.com/76109881/206407957-1e0c5bcc-5244-4e91-bdfd-648788274ba9.png)
## Results

We conclude that in the case of liquidity pools, the volatility of its nature does not lend itself well to being predicted using simple time series analysis on just DAPR values. 

## Future work
1) Enhancing our models by accounting for the individual pools' volatility by using other models in conjunction with ARIMA, such as GARCH to estimate volatility.

2) Instead of just a time series analysis on DAPR values, we could take into account more variables that could contribute to a higher prediction accuracy, such as total amount of liquidity in the pool, or security/faith/sentiment on the exchange the pool is being hosted on, thereby conducting it as a multivariate time series analysis.

