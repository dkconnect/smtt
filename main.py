import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import requests

# Load company data and index data from CSV files
company_data = pd.read_csv('company_data.csv',
                           encoding='ISO-8859-1')  # Adjust encoding as needed
index_data = pd.read_csv('index_fund_data.csv',
                         encoding='ISO-8859-1')  # Adjust encoding as needed

# Create a mapping of indexes to companies
INDEX_COMPANY_MAP = index_data.groupby('Index Fund')['Company'].apply(
    list).to_dict()

# Create a mapping of company to ticker
COMPANY_TICKER_MAP = company_data.set_index('Company')['Ticker'].to_dict()


# Function to get the ticker from the company name
def get_ticker(company_name):
    return COMPANY_TICKER_MAP.get(company_name.strip().title(),
                                  company_name.strip().upper())


st.title("Real-Time Stock Market Tracker")

# Dropdown for selecting an index
selected_index = st.selectbox("Select Stock Index",
                              list(INDEX_COMPANY_MAP.keys()))

# Display companies based on the selected index
selected_company = st.selectbox("Select Company",
                                INDEX_COMPANY_MAP[selected_index])

# Get the ticker for the selected company
ticker = get_ticker(selected_company)

# Fetch and display the latest stock data
data = yf.Ticker(ticker).history(period="1d")
st.write(f"**{ticker}** latest data:")
st.dataframe(data)


# Function to plot historical data
def plot_historical_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'],
                             name='Close Price'))
    fig.layout.update(title_text=f"{ticker} Historical Data",
                      xaxis_rangeslider_visible=True)
    return fig


# Button to show historical data
if st.button("Show Historical Data"):
    fig = plot_historical_data(ticker)
    st.plotly_chart(fig)


# Function to predict stock prices
def predict_stock(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    hist['Date'] = hist.index
    hist['Date'] = hist['Date'].map(pd.Timestamp.toordinal)
    X = hist[['Date']]
    y = hist['Close']
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        shuffle=False)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=X_test['Date'], y=y_test, name='Actual Price'))
    fig.add_trace(
        go.Scatter(x=X_test['Date'], y=y_pred, name='Predicted Price'))
    fig.layout.update(title_text=f"{ticker} Prediction",
                      xaxis_rangeslider_visible=True)
    return fig


# Button to predict stock prices
if st.button("Predict Stock Prices"):
    fig = predict_stock(ticker)
    st.plotly_chart(fig)

# Watchlist functionality
if 'watchlist' not in st.session_state:
    st.session_state['watchlist'] = []

if st.button("Add to Watchlist"):
    st.session_state['watchlist'].append(ticker)

st.write("**Watchlist:**", st.session_state['watchlist'])


# Function to get news articles related to the stock ticker
def get_news(ticker):
    api_key = "3b497bb115a140829ae78f4223188366"  # Replace with your actual API key
    url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json()["articles"]
    return articles


# Button to show news articles
if st.button("Show News"):
    news = get_news(ticker)
    for article in news:
        st.write(f"**{article['title']}**")
        st.write(article['description'])
        st.write(f"[Read more]({article['url']})")

# Add the footer
st.markdown("---")
st.markdown("© 2024 DK - Lucifer. All rights reserved.")
st.markdown("[Visit my GitHub](https://github.com/your-github-username)")
st.markdown("[Source](https://github.com/your-github-username)",
            unsafe_allow_html=True)
