import csv
import requests
import pandas as pd
import  time

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

slice_list=['year1month'+ str(m) for m in list(range(1,13))]
slice_list.extend(['year2month'+ str(m) for m in list(range(1,13))])
list_all_ticker=[]
with requests.Session() as s:
    count=0
    for slice in slice_list:
        CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=' + ticker + \
                  '&interval=1min&slice=' + slice + '&apikey='
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        ticker_list = list(cr)
        print('headers are %s' %ticker_list[0:2] )
        print('length of ticker list is%s' % len(ticker_list) )
        list_all_ticker.append(ticker_list[1:])
        print("len of list now %s"%len(list_all_ticker))
        count=count+1
        if count%5==0:
            time.sleep(60)
print("len",len(list_all_ticker))

import pickle
with open('list_'+ticker+'.ob', 'wb') as fp:
    pickle.dump(list_all_ticker, fp)
