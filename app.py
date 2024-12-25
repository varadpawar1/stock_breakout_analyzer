
import yfinance as yf
import pandas as pd
import streamlit as st

def calculate_breakouts(ticker, start_date, end_date, volume_threshold, price_threshold, holding_period):
    # Fetch data
    data = yf.download(ticker, start=start_date, end=end_date)
    data.columns = data.columns.get_level_values('Price')
    
    # Ensure the DataFrame is not empty
    if data.empty:
        raise ValueError("No data fetched for the given ticker and date range.")
    
    # Calculate 20-day rolling average volume
    data['20DayAvgVolume'] = data['Volume'].rolling(window=20).mean()

    # Identify volume breakout
    data['VolumeBreakout'] = data['Volume'] > (volume_threshold / 100) * data['20DayAvgVolume']

    # Calculate daily percentage change in closing price
    data['PriceChange'] = data['Close'].pct_change() * 100

    # Identify price breakout
    data['PriceBreakout'] = data['PriceChange'] > price_threshold

    # Combine conditions to identify breakout days
    data['Breakout'] = data['VolumeBreakout'] & data['PriceBreakout']

    # Simulate trades
    trades = []
    for i in range(len(data)):
        if data.iloc[i]['Breakout']:
            buy_date = data.index[i]
            sell_date_index = i + holding_period

            # Ensure sell date index is within bounds
            if sell_date_index < len(data):
                sell_date = data.index[sell_date_index]
                buy_price = data.iloc[i]['Close']
                sell_price = data.iloc[sell_date_index]['Close']
                return_percent = ((sell_price - buy_price) / buy_price) * 100
                trades.append({
                    'Buy Date': buy_date,
                    'Sell Date': sell_date,
                    'Buy Price': buy_price,
                    'Sell Price': sell_price,
                    'Return (%)': return_percent
                })

    # Create DataFrame for results
    results = pd.DataFrame(trades)

    return data, results


# Streamlit UI
st.title("Stock Breakout Strategy Analysis")

# User Inputs
ticker = st.text_input("Enter Ticker Symbol (e.g., AAPL):")
start_date = st.date_input("Start Date:")
end_date = st.date_input("End Date:")
volume_threshold = st.number_input("Volume Breakout Threshold (%)", min_value=0, value=200)
price_threshold = st.number_input("Price Change Threshold (%)", min_value=0, value=2)
holding_period = st.number_input("Holding Period (days)", min_value=1, value=10)

# Generate Report
if st.button("Generate Report"):
    try:
        if ticker and start_date and end_date:
            # Run breakout calculation
            data, results = calculate_breakouts(
                ticker, start_date, end_date, volume_threshold, price_threshold, holding_period
            )
            
            # Display results
            st.write("Breakout Days Analysis")
            st.dataframe(results)

            # Provide CSV download
            if not results.empty:
                st.download_button(
                    label="Download CSV",
                    data=results.to_csv(index=False),
                    file_name="breakout_results.csv",
                    mime="text/csv"
                )
            else:
                st.write("No breakout days found for the given parameters.")
        else:
            st.error("Please fill out all fields.")
    except Exception as e:
        st.error(f"Error: {e}")
