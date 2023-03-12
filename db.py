import streamlit as st  
from datetime import date
from pytz import timezone
import plotly.express as px

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

st.set_page_config(page_title = "Prediction",
                   page_icon = ":mag:",
                   layout = "wide")

st.title(":chart_with_upwards_trend: Stock Indices Prediction App")

st.sidebar.write(":mag:Predictions")

box = st.sidebar.radio("🧭 Navigation", ["Home", "Global Indices", "Forecaste"])

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

stocks = ["^NSEI", "^BSESN", "^RUT", "^GSPC", "^DJI", "^NDX", "^HSI", "^N225", "^FCHI"]

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data
    
if box == "Home":
    st.image("https://img.freepik.com/premium-photo/stock-market-forex-trading-graph-graphic-concept_73426-102.jpg?w=2000")
    st.write("******On this Stock Indices Prediction App, you can predict the future 5 years of stock index which is listed on their respective Stock exchange..******")
if box == "Global Indices":
    option = st.sidebar.selectbox("Gloabl Indices", stocks)
    if option == "^NSEI":
        st.subheader("🇮🇳 Nifty 50")
        n_years = st.slider("Years of prediction:", 0, 5)
        period = n_years * 365

        date_load_state = st.text("Load data....")
        data = load_data(option)
        date_load_state.text("Loading data....done!")

        st.subheader('Raw data')
        st.write(data.tail(200))

    if option == "^BSESN":
        st.subheader("🇮🇳 Sensex")
        n_years = st.slider("Years of prediction:", 0, 5)
        period = n_years * 365

        date_load_state = st.text("Load data....")
        data = load_data(option)
        date_load_state.text("Loading data....done!")

        st.subheader('Raw data')
        st.write(data.tail(200))

    if option == "^RUT":
        st.subheader("🇬🇧 Russell 2000")
        n_years = st.slider("Years of prediction:", 0, 5)
        period = n_years * 365

        date_load_state = st.text("Load data....")
        data = load_data(option)
        date_load_state.text("Loading data....done!")

        st.subheader('Raw data')
        st.write(data.tail(200))

    if option == "^GSPC":
        st.subheader("🇺🇸 S&P 500")
        n_years = st.slider("Years of prediction:", 0, 5)
        period = n_years * 365

        date_load_state = st.text("Load data....")
        data = load_data(option)
        date_load_state.text("Loading data....done!")

        st.subheader('Raw data')
        st.write(data.tail(200))

    if option == "^DJI":
        st.subheader("🇺🇸 Dow Jones Industrial Average")
        n_years = st.slider("Years of prediction:", 0, 5)
        period = n_years * 365

        date_load_state = st.text("Load data....")
        data = load_data(option)
        date_load_state.text("Loading data....done!")

        st.subheader('Raw data')
        st.write(data.tail(200))

    if option == "^NDX":
        st.subheader("🇺🇸 NASDAQ 100")
        n_years = st.slider("Years of prediction:", 0, 5)
        period = n_years * 365

        date_load_state = st.text("Load data....")
        data = load_data(option)
        date_load_state.text("Loading data....done!")

        st.subheader('Raw data')
        st.write(data.tail(200))

    if option == "^HSI":
        st.subheader("🇭🇰 HANG SENG INDEX")
        n_years = st.slider("Years of prediction:", 0, 5)
        period = n_years * 365

        date_load_state = st.text("Load data....")
        data = load_data(option)
        date_load_state.text("Loading data....done!")

        st.subheader('Raw data')
        st.write(data.tail(200))

    if option == "^N225":
        st.subheader(":jp: Nikkei 225")
        n_years = st.slider("Years of prediction:", 0, 5)
        period = n_years * 365

        date_load_state = st.text("Load data....")
        data = load_data(option)
        date_load_state.text("Loading data....done!")

        st.subheader('Raw data')
        st.write(data.tail(200))

    if option == "^FCHI":
        st.subheader("🇫🇷 CAC 40")
        n_years = st.slider("Years of prediction:", 0, 5)
        period = n_years * 365

        date_load_state = st.text("Load data....")
        data = load_data(option)
        date_load_state.text("Loading data....done!")

        st.subheader('Raw data')
        st.write(data.tail(200))

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='index_open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='index_close'))
        fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True, height=600, width=850)
        st.plotly_chart(fig)


    plot_raw_data()

# Forecasting
if box == "Forecaste":
    option = st.sidebar.selectbox("Gloabl Indices", stocks)
    data = load_data(option)
    n_years = st.slider("Years of prediction:", 0, 5)
    period = n_years * 365
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    st.subheader('Forecast data')
    st.write(forecast.tail())

    st.write('Forecast data')
    fig1 = plot_plotly(m, forecast) 
    st.plotly_chart(fig1)

    st.write('forecast components')
    fig2 = m.plot_components(forecast)
    st.write(fig2)
