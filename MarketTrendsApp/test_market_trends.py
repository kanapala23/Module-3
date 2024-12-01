import pytest
import pandas as pd
from datetime import datetime
import numpy as np
from market_trends_dashboard import fetch_market_data, predict_future_trends

# Test the fetch_market_data function
def test_fetch_market_data():
    start_date = "2023-01-01"
    end_date = "2023-01-31"
    market_data = fetch_market_data("SPX", start_date, end_date)
    assert not market_data.empty, "Market data should not be empty"
    assert "Date" in market_data.columns, "Market data must have a 'Date' column"
    assert "Price" in market_data.columns, "Market data must have a 'Price' column"

# Test the predict_future_trends function
def test_predict_future_trends():
    data = pd.DataFrame({
        "Date": pd.date_range("2023-01-01", "2023-01-10"),
        "Price": np.random.uniform(100, 500, 10),
    })
    predictions = predict_future_trends(data)
    assert len(predictions) == 5, "Prediction should return 5 future data points"
    assert all(p > 0 for p in predictions), "Predicted prices should be positive"
