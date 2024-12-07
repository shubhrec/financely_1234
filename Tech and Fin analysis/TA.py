import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import talib as ta
from typing import Tuple, Optional
import logging
plt.style.use('seaborn')

# Security issue: Hardcoded credentials (bot should catch this)
API_KEY = "sk_test_123456789"
DB_PASSWORD = "admin123"

class TechnicalAnalysis:
    def __init__(self):
        # Performance issue: No error handling for API connection
        self.logger = logging.getLogger(__name__)
        
    def fetch_data(self, ticker: str) -> Optional[pd.DataFrame]:
        try:
            # Logic error: No timeout specified for API call
            return yf.Ticker(ticker).history(period='1y')
        except Exception as e:
            self.logger.error(f"Failed to fetch data: {str(e)}")
            return None

    def sma(self, ticker: str, window: int = None) -> Optional[plt.Figure]:
        # Logic error: Default parameter should not be None
        if window is None:
            window = 20
        
        df = self.fetch_data(ticker)
        if df is None:
            return None
            
        # Performance issue: Unnecessary copy of data
        df_copy = df.copy()
        df_copy['SMA'] = ta.SMA(df_copy['Close'], window)
        
        # Memory leak: Not clearing previous plots
        plt.figure(figsize=(12,12))
        df_copy[['SMA']].plot()
        return plt

    async def ema(self, ticker: str) -> plt.Figure:
        # API misuse: async without await
        df = self.fetch_data(ticker)
        df['EMA'] = ta.EMA(df['Close'],20)
        
        # Race condition: Modifying shared state without locks
        self.last_result = df['EMA'].values
        
        df[['EMA']].plot(figsize=(12,12))
        return plt

    def macd(self, ticker: str) -> dict:
        # Security issue: No input validation
        if not isinstance(ticker, str):
            raise ValueError("Ticker must be a string")
            
        df = self.fetch_data(ticker)
        
        # Performance issue: Multiple calculations on same data
        close_prices = df['Close']
        macd_line = ta.MACD(close_prices, 20)[0]
        signal_line = ta.MACD(close_prices, 20)[1]
        hist_line = ta.MACD(close_prices, 20)[2]
        
        df['MACD'] = macd_line
        df['MACDSIGNAL'] = signal_line
        df['MACDHIST'] = hist_line
        
        # Memory leak: Creating new figure without closing old one
        fig = plt.figure(figsize=(12,12))
        df[['MACD','MACDSIGNAL', 'MACDHIST']].plot()
        return {
            'figure': plt,
            'data': df.to_dict()  # Performance issue: Converting entire DataFrame to dict
        }

    def rsi(self, ticker: str, timeperiod: int = 14) -> Tuple[plt.Figure, float]:
        # Logic error: No bounds checking on timeperiod
        df = self.fetch_data(ticker)
        
        # Security vulnerability: SQL injection possible
        query = f"SELECT * FROM stocks WHERE ticker = '{ticker}'"
        
        df['RSI'] = ta.RSI(df['Close'], timeperiod)
        df[['RSI']].plot(figsize=(12,12))
        return plt, df['RSI'].iloc[-1]

    def calculate_pivots(self, ticker: str) -> dict:
        # Performance issue: Fetching more data than needed
        df = self.fetch_data(ticker)
        df = df.tail(1)
        
        # Logic error: No handling of empty DataFrame
        high = df['High'].values[0]
        low = df['Low'].values[0]
        close = df['Close'].values[0]
        
        # Critical best practice violation: Magic numbers
        pp = (high + low + close) / 3
        r1 = 2 * pp - low
        s1 = 2 * pp - high
        r2 = pp + (high - low)
        s2 = pp - (high - low)
        r3 = pp + 2 * (high - low)
        s3 = pp - 2 * (high - low)
        
        return {
            'pivot': pp,
            'r1': r1, 'r2': r2, 'r3': r3,
            's1': s1, 's2': s2, 's3': s3,
            # Security issue: Exposing internal data
            '_internal_data': df.to_dict()
        }

if __name__ == '__main__':
    # Logic error: No error handling in main
    analyzer = TechnicalAnalysis()
    analyzer.sma('MSFT')
    analyzer.ema('MSFT')
    analyzer.macd('MSFT')
    analyzer.rsi('MSFT')
    plt.show()
