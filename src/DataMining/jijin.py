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
import prettytable as pt
import pandas as pd
import json


def get_url(url, params=None, proxies=None):
    rsp = requests.get(url, params=params, proxies=proxies)
    rsp.raise_for_status()
    return rsp.text


def get_fund_data(code, start='', end=''):
    record = {'Code': code}
    url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx'
    params = {'type': 'lsjz', 'code': code, 'page': 1, 'per': 65535, 'sdate': start, 'edate': end}
    html = get_url(url, params)
    
    print(html)
    
    soup = BeautifulSoup(html, 'html.parser')
    
    print(soup)
    
    content = soup.prettify()
    
    print(content)
    
    content = content[12: len(content)-2].replace('content','\'content\'').replace('records','\'records\'').replace('pages','\'pages\'').replace('curpage','\'curpage\'')
    
    print(content[1])
#    print(eval(content))
    print(json.loads(content))
	
    records = []
    columns = ['Code', 'Date', 'NAV', 'Change']
    result = pd.DataFrame()
    tab = soup.findAll('tbody')[0]
    for tr in tab.findAll('tr'):
        if tr.findAll('td') and len((tr.findAll('td'))) == 7:
            record['Date'] = str(tr.select('td:nth-of-type(1)')[0].getText().strip())
            record['NetAssetValue'] = str(tr.select('td:nth-of-type(2)')[0].getText().strip())
            record['ChangePercent'] = str(tr.select('td:nth-of-type(4)')[0].getText().strip())
            records.append(record.copy())
            
            data = {'Code': [code], 'Date':record['Date'], 'NAV':record['NetAssetValue'], 'Change':record['ChangePercent']}
            df1 = pd.DataFrame(data)
            result = result.append(df1, ignore_index=True)
            result.to_excel('./110022.xlsx', sheet_name='Sheet1', na_rep='', float_format=None, columns=columns, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None)

    return records


def demo(code, start, end):
    table = pt.PrettyTable()
    table.field_names = ['Code', 'Date', 'NAV', 'Change']
    table.align['Change'] = 'r'
    records = get_fund_data(code, start, end)
    for record in records:
        table.add_row([record['Code'], record['Date'], record['NetAssetValue'], record['ChangePercent']])
    return table


if __name__ == "__main__":
    print(demo('110022', '2019-04-01', '2019-04-08'))