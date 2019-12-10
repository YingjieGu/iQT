# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:45:49 2019

@author: lenovo
"""

import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.linearmodels as snsl

from datetime import datetime
import tushare as ts

sns.set_style("whitegrid")

end = datetime.today() #开始时间结束时间，选取最近一年的数据
start = datetime(end.year-1,end.month,end.day)
end = str(end)[0:10]
start = str(start)[0:10]

stock = ts.get_hist_data('600446',start,end)#选取一支股票
stock['close'].plot(legend=True ,figsize=(10,4))
stock[['close','ma5','ma10','ma20']].plot(legend=True ,figsize=(10,4)) #5日均线、10日均线以及20日均线`

#每日涨跌幅
#stock['Daily Return'] = stock['close'].pct_change()
#stock['Daily Return'].plot(legend=True,figsize=(10,4))

#核密度估计
#sns.kdeplot(stock['Daily Return'].dropna())

#核密度估计+统计柱状图
#sns.distplot(stock['Daily Return'].dropna(),bins=100)

#两支股票的皮尔森相关系数
#sns.jointplot(stock['Daily Return'],stock['Daily Return'],alpha=0.2)


plt.show()