# _*_ coding: utf-8 _*_

import pandas as pd
import datetime as dt
import datetime as dt

# データの読み込み
data = pd.read_csv("../data/raw_data.csv", index_col='id')
data['date'] = pd.to_datetime(data['date'])

thisYear = int(data['date'].max().strftime('%Y'))

# 空データを生成する
with open('../log/getDescribe_by_year.txt', mode='w') as f:
    	print("")

# このスクリプトは年毎の要約統計量を得るためのものです．
while True:
    data_by_y = data[(data['date'] >= dt.datetime(thisYear,1,1)) & (data['date'] <= dt.datetime(thisYear,12,31))]
    
    if(thisYear < int(data['date'].min().strftime('%Y'))):
        break
    print(str(thisYear) + "年:")
    print(data_by_y.describe())
    print("")
    
    with open('../log/getDescribe_by_year.txt', mode='a') as f:
    	f.write(str(thisYear) + "年：\n")
    	f.write(str(data_by_y.describe()) + "\n\n")
    	
    thisYear = thisYear - 1
