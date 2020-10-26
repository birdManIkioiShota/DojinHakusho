# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# 年毎の箱ひげ図を生成するスクリプト

data = pd.read_csv("../data/raw_data.csv")
data['date'] = pd.to_datetime(data['date'])

thisYear = int(data['date'].min().strftime('%Y'))

data_concat = None
while True:
    data_by_y = data[(data['date'] >= dt.datetime(thisYear,1,1)) & (data['date'] <= dt.datetime(thisYear,12,31))]
    if(thisYear > int(data['date'].max().strftime('%Y'))):
        break

    data_by_y = data_by_y.rename(columns={'sales' : str(thisYear)})
    data_by_y = data_by_y[str(thisYear)]
    
    # ここから年毎に別々の図にまとめて出力する処理
    fig, axes = plt.subplots()

    # 表示範囲の設定
    # 外れ値が大きすぎるときに設定すること
    #plt.ylim([0,10000])
    
    plt.title('Box plot of sales in ' + str(thisYear))
    plt.xlabel('Year')
    plt.ylabel('Number of sales')
    plt.boxplot(data_by_y, showmeans=True)
    axes.set_xticklabels([thisYear])
    plt.grid(linestyle='dashed')
    plt.savefig("../fig/Boxplot_" + str(thisYear) + ".png")

    data_by_y = data_by_y.dropna().reset_index(drop=True)
    
    data_concat = pd.concat([data_concat, data_by_y], axis=1)
    thisYear = thisYear + 1

# ここから年毎に1つの図にまとめて出力する処理
fig, axes = plt.subplots()
data_concat_values = data_concat.values
mask = ~np.isnan(data_concat_values)
filtered_data = [d[m] for d, m in zip(data_concat_values.T, mask.T)]

plt.grid(linestyle='dashed')
plt.title('Box plot of sales by year')

# 表示範囲の設定
# 外れ値が大きすぎるときに設定すること
plt.ylim([0, 10000])
plt.xlabel('Year')
plt.ylabel('Number of Sales')
plt.boxplot(filtered_data, showmeans=True)

# x軸のラベル
axes.set_xticklabels(['2016','2017','2018','2019','2020'])

plt.savefig("../fig/Boxplot_by_year.png")
