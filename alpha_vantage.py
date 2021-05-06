import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'LMZHC60IDKQ1WRHX'

ts = TimeSeries(key=api_key, output_format='pandas')
print(ts)

data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')

print("ts:")
print(type(ts))

print("data:")
print(type(data))
print(data.head(3))







#while true:
#    data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
#    data.to_excel("MSFT_out.xlsx")
#    time.sleep(60)

#close_data = data['4. close']
#percentage_change = close_data.pct_change()
#print(percentage_change)

#last_change = percentage_change[-1]

#print('-------------------------------------------------------')
#print('last change')
#print (last_change)
#print('-------------------------------------------------------')

#if abs(last_change) > 0.004:
#    print("MSFT Alert:" + last_change)
