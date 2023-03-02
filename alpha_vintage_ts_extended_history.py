import csv
import requests
import pandas as pd
import  time

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
ticker='SPY'
#slice_list=['year1month'+ str(m) for m in list(range(1,13))]
slice_list=['year2month'+ str(m) for m in list(range(1,13))]
list_all_ticker=[]
with requests.Session() as s:
    count=0
    for slice in ['year2month1','year2month2']:
        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=' + ticker + \
                  '&interval=15min&slice=' + slice + '&apikey='
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        ticker_list = list(cr)
        print('headers are %s' %ticker_list[0] )
        print('headers are %s' % len(ticker_list) )
        list_all_ticker.append(ticker_list)
        print("len of list now %s"%len(list_all_ticker))
        count=count+1
        if count%5==0:
            time.sleep(60)
#print(list_all_ticker)
print("len",(list_all_ticker))
print("first few", list_all_ticker[0])
time.sleep(60)
print("first few", list_all_ticker[0][1:5])
time.sleep(60)
print("first few", list_all_ticker[1][1:5],)
# print(len(list_all_ticker[0]))
df_data = pd.DataFrame(list_all_ticker)
df_data.to_csv('spy.csv')
# print(df_data.tail(5))
