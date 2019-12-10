# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:45:05 2019

@author: fengbingru
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:32:02 2019

@author: fengbingru
"""

import requests
from bs4 import BeautifulSoup
from prettytable import *
import pandas as pd
import time
import re
import matplotlib.pyplot as plt



def get_url(url, params=None, proxies=None):
    rsp = requests.get(url, params=params, proxies=proxies)
    rsp.raise_for_status()
    return rsp.text


filepath = './' + '110022-' + '-' + time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.xlsx'
writer = pd.ExcelWriter(filepath)
result = pd.DataFrame()
pages = None
columns = ['Code', 'Date', 'NAVE', 'Change']
def get_fund_data(code, page, start='', end=''):
    page = (page==None) and 1 or page
#    print(page)
    record = {'Code': code}
    url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx'
    params = {'type': 'lsjz', 'code': code, 'page': page, 'per': 5, 'sdate': start, 'edate': end}
    html = get_url(url, params)
    soup = BeautifulSoup(html, 'html.parser')
    totalRecord = soup.prettify()
    global pages
    pages = re.findall(".*pages:(.*),.*",totalRecord)[0]
    records = []
    global result
    tab = soup.findAll('tbody')[0]
    
    print(tab)
    
    for tr in tab.findAll('tr'):
        if tr.findAll('td') and len((tr.findAll('td'))) == 7:
            record['Date'] = str(tr.select('td:nth-of-type(1)')[0].getText().strip())
            record['NetAssetValue'] = str(tr.select('td:nth-of-type(2)')[0].getText().strip())
            record['ChangePercent'] = str(tr.select('td:nth-of-type(4)')[0].getText().strip())
            records.append(record.copy())
            
            data = {'Code': [code], 'Date':record['Date'], 'NAVE':record['NetAssetValue'], 'Change':record['ChangePercent']}
            df1 = pd.DataFrame(data, index = [0])
            result = result.append(df1, ignore_index=True)
    
    if page <= int(pages):
        get_fund_data(code, page+1, start, end)
    else:
#        result.set_index('Date', inplace=True)
        
        result=result['NAVE'].astype(float)
        print(result)
        
        ax = result.plot()
        ax.set_title("NAVE")
        ax.set_ylabel('NAVE')
#        ax.set_xticklabels(result['Date'])
        ax.grid(linestyle="--", alpha=0.3)
        plt.show()
        
#        result.to_excel(excel_writer=writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=columns, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None)
        result.to_excel(excel_writer=writer, sheet_name='Sheet1', merge_cells=True)
        writer.save()
        writer.close()
    
    return records


def demo(code, start, end):
    get_fund_data(code, None, start, end)

if __name__ == "__main__":
    for year in ['2014', '2015', '2016', '2017', '2018', '2019']:
        print(year)
#        print(demo('110022', year+'-04-01', year+'-05-10'))
        print(demo('110022', year+'-01-01', year+'-03-01'))
#        print(demo('600519', year+'-09-01', year+'-10-15'))