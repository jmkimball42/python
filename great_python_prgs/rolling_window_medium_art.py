# Import necessary libraries
#%matplotlib inline
from zipline import run_algorithm
from zipline.api import order_target_percent, symbol, set_commission
from zipline.finance.commission import PerTrade
import pandas as pd
import pyfolio as pf
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Initialize the trading algorithm
def initialize(context):
    context.stock = symbol('AAPL')             # Stock symbol for Apple Inc.
    context.rolling_window = 90                # Define a rolling window of 90 days
    set_commission(PerTrade(cost=0))           # Set the commission cost per trade

# Define the handling of data for each trading step
def handle_data(context, data):
    # Retrieve historical price data
    price_hist = data.history(context.stock, "close", context.rolling_window, "1d")
    # Place an order based on the comparison of the latest price to the mean
    order_target_percent(context.stock, 1.0 if price_hist[-1] > price_hist.mean() else 0.0)

# Perform analysis after the run
def analyze(context, perf):
    returns, positions, transactions = pf.utils.extract_rets_pos_txn_from_zipline(perf)
    pf.create_returns_tear_sheet(returns, benchmark_rets=None)

# Define start and end dates for the backtest
start_date = pd.to_datetime('2018-1-1', utc=True)
end_date = pd.to_datetime('2023-8-14', utc=True)

# Execute the algorithm
results = run_algorithm(start=start_date, end=end_date,
                        initialize=initialize,
                        analyze=analyze,
                        handle_data=handle_data,
                        capital_base=10000,
                        data_frequency='daily',
                        bundle='quandl')