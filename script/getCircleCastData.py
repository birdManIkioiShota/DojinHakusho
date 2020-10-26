# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import collections

data = pd.read_csv("../data/raw_data.csv", index_col='id')
data['date'] = pd.to_datetime(data['date'])

# 空データの生成
f = open('../log/getCircleCastData.txt', mode='w')

# サークル出現数の閾値
circle_n_thr = 3

# サークル出現数の記述
title = ("サークル出現数(>= " + str(circle_n_thr) + ")：")
info = (str(data['circle'][data['circle'].map(data['circle'].value_counts() >= circle_n_thr)].value_counts()))
print(title + "\n" + info)
f.write(title + "\n" + info)

# 調査対象の声優を排除する
exc_cast = "砂糖しお"

spl_cast = data['cast'].str.split(',', expand=True)

castData = None
for clnm in spl_cast:
    spl_cast.loc[spl_cast[clnm] == exc_cast] = None
    castData = pd.concat([castData, spl_cast[clnm]])

title = ("声優出現数(exclude " + exc_cast + ")")
info = str(castData.value_counts())
print("\n" + title + "\n" + info)
f.write("\n\n" + title + "\n" + info)
f.close()
