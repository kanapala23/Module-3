import streamlit as st
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

# Function to fetch market data (mock implementation)
def fetch_market_data(market_symbol, start_date, end_date):
    dates = pd.date_range(start_date, end_date)
    prices = np.random.uniform(100, 500, len(dates))  # Simulated prices
    return pd.DataFrame({"Date": dates, "Price": prices})

# Function to predict future trends using machine learning
def predict_future_trends(data):
    data["Day"] = range(len(data))
    model = LinearRegression()
    model.fit(data[["Day"]], data["Price"])
    future_days = [[len(data) + i] for i in range(1, 6)]  # Predict next 5 days
    predictions = model.predict(future_days)
    return predictions

# Streamlit app function
def generate_market_trends_dashboard():
    st.title("Market Trends Analysis")

    # User input for date range and market symbol
    date_range = st.date_input("Select Date Range", [datetime(2023, 1, 1), datetime(2023, 1, 31)])
    market_symbol = st.text_input("Enter Market Symbol", "SPX")

    # Button to fetch data
    if st.button("Fetch Data"):
        if len(date_range) == 2:
            start_date, end_date = date_range
            market_data = fetch_market_data(market_symbol, start_date, end_date)
            st.write(f"Fetched data for {market_symbol} from {start_date} to {end_date}")
            st.dataframe(market_data)

            # Generate and display market trend predictions
            predictions = predict_future_trends(market_data)
            st.write("Future Trend Predictions (next 5 days):")
            for i, price in enumerate(predictions, 1):
                st.write(f"Day {i}: ${price:.2f}")
        else:
            st.error("Please select a valid date range.")

if __name__ == "__main__":
    generate_market_trends_dashboard()
