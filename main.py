import alphav
from matplotlib import pyplot as plt
import numpy as np


### API PARAMETERS #############################################################
#   - [symbol]     = name of equity
#   - [interval]   = interval btwn 2 consecutive data points in time series.
#   - [adjusted]   = output time series is adjusted by historical split data and 
#                    dividen events.
#
#   - [outputsize] = [compact] returns only the latest 100 data points in the
#                    intraday time series; [full] returns full-length intraday
#                    time series.
#
#   - [datatype]   = Returns data in either JSON or CSV format.
#
#   - [slice]      = 2 years of intraday data is evenly divided into 24 slices.
#                    Each slice is a 30-day window, with year1month1 being the 
#                    most recent and year2month12 being the farthest from today.
#                    Values can be: 
#             [year1month1], [year1month2], ..., [year1month11], [year1month12], 
#             [year2month1], [year2month2], ..., [year2month11], [year2month12].
#
#   - [tickers]    = The stock/crypto/forex symbols of your choice, i.e.
#                    [tickers=IBM].
#   - [topics]     = The news topice of your choice, i.e. [topics=technology].
#
#   - [time_from]  = Time range of the news articles you are targeting,
#     [time_to]      in YYYYMMDDTHHMM format. i.e. [time_from=20220410T0130].
#                    If [time_to] is not specified, current time will be used.
#
#   - [sort]       = [sort=LATEST] returns the latest articles first. Can be
#                    also set using [sort=EARLIEST] and [sort=RELEVANCE].
#
#   - [limit]      = By defualt, [limit=50] will return 50 matching results.
################################################################################

### FUNCTION ###
################################################################################
# [TIME_SERIES_INTRADAY]           [symbol], 
#                                  [interval=1min/10min/15min/30min/60min],
#                                 ([outputsize=full]),
#                                 ([adjusted=true/false]),
#                                 ([datatype=json/csv])
#
# Returns the most recent 1-2 months of intraday data. Best suited for
# short-term/medium-term charting. Covers extended trading hours (4AM-8PM EST).
################################################################################
# [TIME_SERIES_INTRADAY_EXTENDED]  [symbol], 
#                                  [interval=1min/10min/15min/30min/60min],
#                                  [slice],
#                                 ([adjusted=true/false])
#
# Returns historical intraday time series for the trailing 2 years, covering
# over 2mil data points per ticker.
################################################################################
# [TIME_SERIES_DAILY_ADJUSTED]     [symbol],
#                                 ([outputsize=compact/full]),
#                                 ([datatype=json/csv])
#
# Returns raw daily open/high/low/close/volume values, daily adjusted close
# values, and historical split/dividen events of the global equity specified,
# covering 20+ years of historical data.
################################################################################
# [TIME_SERIES_WEEKLY]             [symbol],
#                                 ([datatype=json/csv])
#
# Returns weekly time series (last trading day of each week, weekly open,
# weekly high, weekly low, weely close, weekly volume).
################################################################################
# [TIME_SERIES_WEEKLY_ADJUSTED]    [symbol],
#                                 ([datatype=json/csv])
#
# Return weekly adjusted time series (last trading day of each week, weekly
# open, weekly high, weekly low, weely close, weekly volume).
################################################################################
# [TIME_SERIES_MONTHLY]            [symbol],
#                                 ([datatype=json/csv])
#
# Returns monthly time series (last trading day of each month, monthly open,
# monthly high, monthly low, monthly close, monthly volume).
################################################################################
# [TIME_SERIES_MONTHLY_ADJUSTED]   [symbol],
#                                 ([datatype=json/csv])
#
# Returns monthly adjusted time series (last trading day of each month, monthly
# open, monthly high, monthly low, monthly close, monthly volume).
################################################################################
# [NEWS_SENTIMENT] ([tickers])
#                  ([topics])
#                  ([time_from])
#                  ([time_to])
#                  ([limit])
#
# Returns live and historical market news/sentiment data derived from over 50
# major financial outlets around the world.
#
#///////////////////////////////////////////////////////////////////////////////


if __name__ == '__main__':
    symbol = 'IBM'
    interval = '60min'
    tslice = 'year1month1'


    y1m1_60m = alphav.getIntradayExt(symbol, interval, tslice)
    print("\nGetting intraday IBM data from year 1 month 1 in 60min intervals")
    print("////////////////////////////////////////////////////////////////////////////////")
    print(y1m1_60m)
    print("ndim={}, shape={}, size={}".format(y1m1_60m.ndim, y1m1_60m.shape, y1m1_60m.size))
    print("////////////////////////////////////////////////////////////////////////////////")
    plt.title("IBM data year1 month 1")
    plt.xlabel("Opening price")
    plt.ylabel("Time")
    plt.plot(y1m1_60m[:,1])
    plt.show()

    
    #interval='15min'
    #y1m1_15m = alphav.getIntradayExt(symbol, interval, tslice)
    #print("\nGetting intraday IBM data from year 1 month 1 in 60min intervals")
    #print("////////////////////////////////////////////////////////////////////////////////")
    #print(y1m1_15m)
    #print("ndim={}, shape={}, size={}".format(y1m1_15m.ndim, y1m1_15m.shape, y1m1_15m.size))
    #print("////////////////////////////////////////////////////////////////////////////////")
