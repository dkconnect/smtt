# Stock Market Trading Tool
Using Streamlib, Pandas, Numpy, Matplotlib etc.

# Dataset:
You will find 2 datasets company_data.csv and index_fund_data.csv. The CSV files have list of companies, index fund, ticker and currency. 

# Main File
You can find the requirements in requirements.txt, I have used replit for development. 
You need to install all the libraries and then get an API Key from newsapi.org

![tt3](https://github.com/dkconnect/smtt/blob/main/choose%20company.png)

# Test:
Test accuracy metric is root mean square error (RMSE).
# Results:
The comparison of OHLC, HLC and Closing price:

![ttt1](https://user-images.githubusercontent.com/24511419/29501710-76018bbe-864c-11e7-9239-afd8bbf19bb8.png)

After the training the fitted curve with original stock price:

![tt2](https://user-images.githubusercontent.com/24511419/29501783-eb7eccd0-864c-11e7-9c26-0db07dea73c0.png)

# Observation and Conclusion:
Since difference among OHLC average, HLC average and closing value is not significat, so only OHLC average is used to build the model and prediction. The training and testing RMSE are: 1.24 and 1.37 respectively which is pretty good to predict future values of stock.
Stock price of last day of dataset was 158.8745 and using this model and price of next two days are predicted as 160.3230 and 160.9240 - which were 159.2075 and 159.8325 on 14th and 15th August 2017 according to Yahoo Finance. However, future values for any time period can be predicted using this model.

Finally, this work can greatly help the quantitative traders to take decisions.

