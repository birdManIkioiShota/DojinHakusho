# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# 年毎の箱ひげ図を生成するスクリプト

data = pd.read_csv("../data/raw_data.csv", index_col='id')
data['date'] = pd.to_datetime(data['date'])

thisYear = int(data['date'].min().strftime('%Y'))

data_concat = None
while True:
    data_by_y = data[(data['date'] >= dt.datetime(thisYear,1,1)) & (data['date'] <= dt.datetime(thisYear,12,31))]
    if(thisYear > int(data['date'].max().strftime('%Y'))):
        break

    data_by_y= data_by_y.rename(columns={'sales' : str(thisYear)})
    data_by_y = data_by_y[str(thisYear)]
    
    fig, axes = plt.subplots()
    plt.ylim([0,10000])
    plt.title('Box plot of sales in ' + str(thisYear))
    plt.xlabel('Term')
    plt.ylabel('Number of sales')
    plt.boxplot(data_by_y, showmeans=True)
    axes.set_xticklabels([thisYear])
    plt.grid(linestyle='dashed')
    plt.savefig("../fig/Boxplot_" + str(thisYear) + ".png")
    
    data_concat = pd.concat([data_concat, data_by_y], axis=1)
    thisYear = thisYear + 1
