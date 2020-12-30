from finviz.screener import Screener

#filters = ['exch_nasd', 'idx_sp500']  # Shows companies in NASDAQ which are in the S&P500
filters = ['idx_sp500', 'ta_rsi_nob50']
stock_list = Screener(filters=filters, table='Performance', order='rsi')  # Get the performance table and sort it by price ascending

# Export the screener results to .csv
stock_list.to_csv("rsistock.csv")

# Create a SQLite database
stock_list.to_sqlite("rsistock.sqlite3")

for stock in stock_list[0:5]:  # Loop through 10th - 20th stocks
        print(stock['Ticker'], stock['Price']) # Print symbol and price

        # Add more filters
        #stock_list.add(filters=['fa_div_high'])  # Show stocks with high dividend yield
        #stock_list(filters=['fa_div_high'])

        # Print the table into the console
        #print(stock_list)
