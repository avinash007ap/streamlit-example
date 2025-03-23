import streamlit as st
import pandas as pd
import yfinance as yf  # If using stock data

top_stocks = ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "BRK.B", "AVGO", "WMT"]

@st.cache_data
def fetch_stock_data(symbol, start_date, end_date):
    return yf.download(stock_symbol, start=start_date, end=end_date)

st.title("📈 Stock Market Dashboard")

if "selected_stock" not in st.session_state:
    st.session_state.selected_stock = "AAPL" 

# User Inputs
stock_symbol = st.pills("Enter Stock Symbol (e.g., AAPL, TSLA):", top_stocks, default=st.session_state.selected_stock)
if stock_symbol:
    date_range = st.date_input("Select Date Range", [])
    chart_cols = ["Close", "High", "Low", "Open", "Volume"]
    chart_columns = [ c + "_" + str(stock_symbol) for c in chart_cols]
    columns = st.multiselect("Select the columns to be displayed", chart_columns, "Close" +  "_" + str(stock_symbol))

    try:
        start_date = date_range[0] if date_range[0] != None else "2024-01-01"
        end_date = date_range[1] if date_range[1] != None else "2024-03-01"
    except:
        start_date = "2024-01-01"
        end_date = "2024-03-01"

# Fetch Stock Data
if stock_symbol and start_date and end_date:
    stock_data = fetch_stock_data(stock_symbol, start_date, end_date)
    st.write("### Stock Data Overview", stock_data.tail())

    if isinstance(stock_data.columns, pd.MultiIndex):
        stock_data.columns = ['_'.join(col).strip() for col in stock_data.columns]
        print("stock_data.columns", stock_data.columns)

    selected_cols = [col for col in stock_data.columns if col in columns]
    selected_columns = [item for item in selected_cols if not item.startswith("Vol")]

    # Line Chart  
    st.line_chart(stock_data[selected_columns])
    if "Volume_" + str(stock_symbol) in selected_cols:
        st.line_chart(stock_data["Volume_" + str(stock_symbol)], x_label="Volume_" + str(stock_symbol))

    # Download Option
    st.download_button("Download Data", stock_data.to_csv(), "stock_data.csv")
