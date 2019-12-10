# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:51:51 2019

@author: lenovo
"""

import pandas_datareader.data as web
import requests
from bs4 import BeautifulSoup
from prettytable import *
import pandas as pd
import time
import datetime
import re
import matplotlib.pyplot as plt


def draw(startdate, endday, code, plat):
    s = startdate.split('-')
    e = endday.split('-')
    start = datetime.datetime(int(s[0]), int(s[1]), int(s[2]))#获取数据的时间段-起始时间
    print(start)
    end = datetime.datetime(int(e[0]), int(e[1]), int(e[2]))#获取数据的时间段-结束时间
    stock = web.DataReader(code, plat, start, end)#获取浙大网新2017年1月1日至今的股票数据
    
    print(stock)
    
    stock = stock['Close'].astype(float)
    
    ax = stock.plot()
    ax.set_title("Close")
    ax.set_ylabel('Close')
    #ax.set_xticklabels(result['Date'])
    ax.grid(linestyle="--", alpha=0.3)
    plt.show()


if __name__ == "__main__":
    for year in ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']:
        print(draw(year+'-10-01', str(int(year)+1)+'-05-28', "600519.SS", "yahoo"))
#        break