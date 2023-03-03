import pickle
import pandas as pd
ticker='SPY'
ticker_data='list_'+ticker+'.ob'
with open (ticker_data, 'rb') as fp:
    list_ticker = pickle.load(fp)

df=pd.concat([pd.DataFrame(d, columns=['time', 'open', 'high', 'low', 'close', 'volume']) for d in list_ticker], ignore_index=True)

print(df.head(5))
print(df.tail(5))
df.to_csv(ticker+'.csv')