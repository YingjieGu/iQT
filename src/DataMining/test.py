# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:54:51 2019

@author: lenovo
"""

''' 
pandas 数据分析
'''

import pandas as pd
import time


'''
###----------表格处理-----------###
'''

'''#创建表格'''
df = pd.DataFrame({"ID": ["A1001","A1002","A1002", "A1000"],"departmentId": [60001,60002, 60003, 60004]})
print('创建表格', df)




'''#删除重复'''
#DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
#subset : column label or sequence of labels, optional 
#用来指定特定的列，默认所有列
#keep : {‘first’, ‘last’, False}, default ‘first’ 
#删除重复项并保留第一次出现的项
#inplace : boolean, default False 
#是直接在原来数据上修改还是保留一个副本
df.drop_duplicates('ID', 'first', inplace=True)
print('删除重复',df)


'''#按值进行排序'''
df = df.sort_values(by='ID')
print('按值进行排序', df)


'''#翻转数据'''
print('翻转数据',df.T)










'''#excel表格的读写'''
#read_excel(io, sheetname=0, header=0, skiprows=None, skip_footer=0, index_col=None,names=None, parse_cols=None, parse_dates=False,date_parser=None,na_values=None,thousands=None, convert_float=True, has_index_names=None, converters=None,dtype=None, true_values=None, false_values=None, engine=None, squeeze=False, **kwds)
#io : string, path object ; excel 路径。
#sheetname : string, int, mixed list of strings/ints, or None, default 0 返回多表使用sheetname=[0,1],若sheetname=None是返回全表 注意：int/string 返回的是dataframe，而none和list返回的是dict of dataframe
#header : int, list of ints, default 0 指定列名行，默认0，即取第一行，数据为列名行以下的数据 若数据不含列名，则设定 header = None
#skiprows : list-like,Rows to skip at the beginning，省略指定行数的数据
#skip_footer : int,default 0, 省略从尾部数的int行数据
#index_col : int, list of ints, default None指定列为索引列，也可以使用u”strings”
#names : array-like, default None, 指定列的名字。

#to_excel(self, excel_writer, sheet_name='Sheet1', na_rep='', float_format=None,columns=None, header=True, index=True, index_label=None,startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None,
#inf_rep='inf', verbose=True, freeze_panes=None)
#- excel_writer : string or ExcelWriter object File path or existing ExcelWriter目标路径
#- sheet_name : string, default ‘Sheet1' Name of sheet which will contain DataFrame,填充excel的第几页
#- na_rep : string, default ”,Missing data representation 缺失值填充
#- float_format : string, default None Format string for floating point numbers
#- columns : sequence, optional，Columns to write 选择输出的的列。
#- header : boolean or list of string, default True Write out column names. If a list of string is given it is assumed to be aliases for the column names
#- index : boolean, default True，Write row names (index)
#- index_label : string or sequence, default None， Column label for index column(s) if desired. If None is given, andheader and index are True, then the index names are used. A sequence should be given if the DataFrame uses MultiIndex.
#- startrow :upper left cell row to dump data frame
#- startcol :upper left cell column to dump data frame
#- engine : string, default None ，write engine to use - you can also set this via the options，io.excel.xlsx.writer, io.excel.xls.writer, andio.excel.xlsm.writer.
#- merge_cells : boolean, default True Write MultiIndex and Hierarchical Rows as merged cells.
#- encoding: string, default None encoding of the resulting excel file. Only necessary for xlwt,other writers support unicode natively.
#- inf_rep : string, default ‘inf' Representation for infinity (there is no native representation for infinity in Excel)
#- freeze_panes : tuple of integer (length 2), default None Specifies the one-based bottommost row and rightmost column that is to be frozen

#读取
data = pd.read_excel('110022.xlsx')
print(data)

#写文件
filePath = './' + 'temp' + '-' + time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.xlsx'
df.to_excel(filePath, sheet_name='Sheet1')


