import csv
import requests
import pandas as pd
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
ticker='UBER'
slice_list=['year1month1','year1month2']

list_all_ticker=[]
with requests.Session() as s:
    for slice in slice_list:
        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=' + ticker + \
                  '&interval=15min&slice=' + slice + '&apikey='
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        ticker_list = list(cr)
        print('headers are %s' %ticker_list[0])
        list_all_ticker.append(ticker_list[2:])

df_data = pd.DataFrame(list_all_ticker[0])
print(df_data.head(5))
