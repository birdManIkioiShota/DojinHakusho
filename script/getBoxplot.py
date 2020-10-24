# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# 全期間の箱ひげ図を生成するスクリプト

data = pd.read_csv("../data/raw_data.csv", index_col='id')
data['date'] = pd.to_datetime(data['date'])

# 箱ひげ図
fig, axes = plt.subplots()
plt.boxplot(data['sales'], showmeans=True)
plt.title('Box plot of sales')
plt.xlabel('Term')
plt.ylabel('Number of sales')

# 表示範囲の設定
# 外れ値が大きすぎる場合箱が隅に追いやられてしまうので使うこと
plt.ylim([0,10000])

axes.set_xticklabels([str(data['date'].min().strftime('%Y/%m/%d')) + " ~ " + str(data['date'].max().strftime('%Y/%m/%d'))])
plt.grid(linestyle='dashed')

plt.savefig("../fig/Boxplot.png")
