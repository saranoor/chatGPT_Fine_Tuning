import yfinance as yf
import pandas as pd
ticker = ['SPY', 'AAPL', 'UBER', 'NFLX', 'AMZN', 'GOOGL','QQQ','TSLA','META','MSFT','QYLD', 'XOM','GE','DIS']
columns = ['Ticker', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
df_all = pd.DataFrame(columns=columns)
for t in ticker:
    data = yf.download(tickers=t,  # list of tickers
                       period="5y",  # time period
                       interval="1d",  # trading interval
                       ignore_tz=True,  # ignore timezone when aligning data from different exchanges?
                       prepost=False)  # download pre/post market hours data?
    data['Ticker']=t
    df_all = pd.concat([df_all, data])
    print(df_all.head())
df_all.to_csv('stock_data.csv', mode='a')

    #data.to_csv('stock_data.csv', mode='a', columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'],header=None)
    # print(data.head())
# data = yf.download(tickers=ticker,  # list of tickers
#                    period="10m",  # time period
#                    interval="1h",  # trading interval
#                    ignore_tz=True,  # ignore timezone when aligning data from different exchanges?
#                    prepost=False)  # download pre/post market hours data?
# data.to_csv('stock_data'+'.csv')
# print(data.columns)
