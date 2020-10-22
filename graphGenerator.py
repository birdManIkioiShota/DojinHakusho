# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DojinHakushoをご利用いただきありがとうございます．
# 本ツールはDLsiteをクロールし，サークル・声優の出演作情報を取得，図表としてレポートする機能を持ちます．
# 現在は販売中の男性向けオーディオファイルに対応しています．
# 詳細につきましては以下URLをご参照ください．
# https://github.com/birdManIkioiShota/DoujinHakusho

# ここに調べたいサークルの名前を入力する．
# 名前はDLsiteのサークル名と一致させる必要がある
# サークル不問の場合は空欄にすること
circle_name = ""

# ここに調べたい声優の名前を入力する．
# 名前はDLsiteのクリエイタータグと一致させる必要がある．
# 声優不問の場合は空欄にすること
creator_name = "砂糖しお"

data = pd.read_csv("data/raw_data.csv", index_col='id')
#data = data[["price", "sales"]]
#print(data.describe())

data['date'] = pd.to_datetime(data['date'])

#data = data[['sales']]
fig, axes = plt.subplots(figsize = (12, 8))
plt.boxplot(data['sales'])
axes.set_xticklabels(['2016-01-23 ~ 2020-10-22'])
plt.grid()
plt.show()

# 年ごとの統計
#data = data[['date', 'sales']]
#data.set_index('date', inplace=True)
#print(data.resample('Y').sum())
# sale sum

# ログのヒストグラム
#plt.hist(data['sales'], bins=np.logspace(1,5,int(np.sqrt(len(data)))))
#plt.gca().set_xscale("log")
#plt.show()
