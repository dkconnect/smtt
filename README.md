# Real-Time Stock Market Tracker

## Overview
The **Real-Time Stock Market Tracker** is a Streamlit web application that provides real-time stock market tracking, historical data visualization, stock price prediction, watchlist functionality, and related news articles for selected stocks.

## Features
- **Stock Selection by Index**: Choose a stock index and select a company from it.
- **Real-Time Stock Data**: Fetch the latest stock prices using Yahoo Finance.
- **Historical Data Visualization**: Display historical price trends using interactive Plotly charts.
- **Stock Price Prediction**: Predict future stock prices using Linear Regression.
- **Watchlist Functionality**: Add selected stocks to a personal watchlist.
- **Stock News Updates**: Retrieve and display the latest news articles related to the selected stock using NewsAPI.

## Technologies Used
- **Python**
- **Streamlit**: For building the interactive web app.
- **Yahoo Finance (yfinance)**: To fetch real-time stock data.
- **Pandas**: For data manipulation.
- **Plotly**: For data visualization.
- **Scikit-learn**: For Linear Regression-based stock price prediction.
- **Requests**: To fetch news articles from NewsAPI.

## Installation
### Prerequisites
Ensure you have Python installed (version 3.x recommended).

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/dkconnect/smtt.git
   ```
2. Navigate to the project directory:
   ```sh
   cd smtt
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Select a stock index and choose a company.
2. View real-time stock data.
3. Click **Show Historical Data** to see stock price trends.
4. Click **Predict Stock Prices** to generate stock price predictions.
5. Click **Add to Watchlist** to save stocks for future tracking.
6. Click **Show News** to fetch the latest news articles.

## API Key Setup
To enable the news fetching feature, replace the placeholder API key in the `get_news` function with your NewsAPI key. You can obtain one at [NewsAPI](https://newsapi.org/).

## License
© 2024 DK - Lucifer. All rights reserved.

## Author
[DK - Lucifer](https://github.com/dkconnect)

