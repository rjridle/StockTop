import numpy as np
import requests
import csv
# Documentation: https://www.alphavantage.co/documentation/
access_key = 'XBS8L3EHOL79MG08'

### Functions ###
# ['time' 'open' 'high' 'low' 'close' 'volume']
#///////////////////////////////////////////////////////////////////////////////
def getIntraday(symbol, interval, outputsize=50, adjusted='false', datatype='csv'):
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval={}&outputsize={}&apikey={}&datatype={}'.format(symbol, interval, outputsize, access_key, datatype)
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return np.delete(arr, (0), axis=0)

################################################################################
def getIntradayExt(symbol, interval, tslice, adjusted='false'):
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={}&interval={}&slice={}&adjusted={}&apikey={}'.format(symbol, interval, tslice, adjusted, access_key)
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        arr = np.array(list(cr))
        #return np.delete(arr, (0), axis=0)
        return arr

################################################################################

def getDailyAdj(symbol, outputsize='full', datatype='csv'):
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize={}&datatype={}&apikey={}&datatype={}'.format(symbol, outputsize, access_key, datatype)
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return np.delete(arr, (0), axis=0)

################################################################################
def getWeekly(symbol, datatype='csv'):
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey={}&datatype={}'.format(symbol, access_key, datatype)
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return np.delete(arr, (0), axis=0)

################################################################################
def getWeeklyAdj(symbol, datatype='csv'):
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={}&apikey={}&datatype={}'.format(symbol, access_key, datatype)
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return np.delete(arr, (0), axis=0)

################################################################################
def getMonthly(symbol, datatype='csv'):
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={}&apikey={}&datatype={}'.format(symbol, access_key, datatype)
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        return np.delete(arr, (0), axis=0)

################################################################################
def getMonthlyAdj(symbol, datatype='csv'):
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={}&apikey={}&datatype={}'.format(symbol, access_key, datatype)
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return np.delete(arr, (0), axis=0)
#///////////////////////////////////////////////////////////////////////////////
