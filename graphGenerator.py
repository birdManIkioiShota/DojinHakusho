# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# DojinHakushoをご利用いただきありがとうございます．
# 本ツールはDLsiteをクロールし，サークル・声優の出演作情報を取得，図表としてレポートする機能を持ちます．
# 現在は販売中の男性向けオーディオファイルに対応しています．
# 詳細につきましては以下URLをご参照ください．
# https://github.com/birdManIkioiShota/DoujinHakusho

data = pd.read_csv("data/raw_data.csv", index_col='id')
#data = data[["price", "sales"]]
#print(data.describe())

data['date'] = pd.to_datetime(data['date'])

#data = data[['sales']]

# 箱ひげ図
fig, axes = plt.subplots(figsize = (12, 8))
plt.boxplot(data['sales'])
plt.title('box plot')
plt.ylabel('sales')
#plt.ylim([0,7500])
axes.set_xticklabels(['all terms'])
plt.grid()
plt.show()

# 年ごとの統計
#data = data[['date', 'sales']]
#data.set_index('date', inplace=True)
#print(data.resample('Y').sum())
# sale sum

