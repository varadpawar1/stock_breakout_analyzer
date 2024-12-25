# Stock Breakout Analyzer

A web-based application to analyze stock trading strategies based on volume and price breakouts. This tool identifies breakout days where a stock’s volume and price movement exceed user-defined thresholds and simulates trading performance over a specified holding period. 

Hosted App: [Click Here to Access the App](https://stockbreakoutanalyzer-ctwwegibqtagapqb8rfzxv.streamlit.app/)

---

## Features

- **Historical Data Fetching**: Uses `yfinance` to retrieve stock data, including daily volume and closing prices.
- **Breakout Detection**:
  - Calculates 20-day rolling average volumes to identify volume breakouts.
  - Detects price breakouts based on daily percentage changes.
- **Trade Simulation**: Simulates buying the stock on breakout days and holding it for a user-defined period to evaluate returns.
- **Interactive UI**: Built with Streamlit, allowing users to input stock tickers, thresholds, and holding periods in real-time.
- **CSV Export**: Allows users to download analysis results for further review.

---

## Usage

1. Visit the hosted app.
2. Enter the following parameters:
   - **Ticker**: Stock symbol (e.g., AAPL, TSLA).
   - **Start Date** and **End Date**: Date range for historical data analysis.
   - **Volume Breakout Threshold (%)**: Minimum percentage by which the day’s volume must exceed the 20-day average.
   - **Price Change Threshold (%)**: Minimum percentage increase in stock price compared to the previous day.
   - **Holding Period (days)**: Number of days to hold the stock after a breakout.
3. Click **"Generate Report"** to analyze breakout days and view simulated returns.
4. Download the results as a CSV file for detailed analysis.

---

## Example Output

**Input Parameters**:
- Ticker: AAPL
- Start Date: 2023-01-01
- End Date: 2023-12-31
- Volume Breakout Threshold: 200%
- Price Change Threshold: 2%
- Holding Period: 10 days

**Output**:
A downloadable CSV file with columns:
- Buy Date
- Sell Date
- Buy Price
- Sell Price
- Return (%)

---

## Installation (For Local Use)

To run the app locally, follow these steps:

### Prerequisites
- Python 3.8 or higher
- Pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/varadpawar1/stock_breakout_analyzer.git
   cd stock_breakout_analyzer
