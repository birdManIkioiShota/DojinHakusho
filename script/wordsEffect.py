# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import datetime as dt
import collections
from scipy import stats

data = pd.read_csv("../data/raw_data.csv", index_col=0)
data['date'] = pd.to_datetime(data['date'])

data_a = data[data["title"].str.contains("バイノーラル") | data["title"].str.contains("KU") | data["title"].str.contains("ハイレゾ")]
data_b = data[~(data["title"].str.contains("バイノーラル") | data["title"].str.contains("KU") | data["title"].str.contains("ハイレゾ"))]

plt.figure()
plt.rcParams['axes.axisbelow'] = True
plt.grid(linestyle='dashed')
plt.hist(data_a['sales'], bins=np.logspace(1,5,int(np.sqrt(len(data_a)))), ec='black', alpha=0.3, color='r', label='特定単語あり')
plt.hist(data_b['sales'], bins=np.logspace(1,5,int(np.sqrt(len(data_b)))), ec='black', alpha=0.3, color='b', label='特定単語なし')

plt.gca().set_xscale("log")

plt.title("Sales histogram (log scale)")
plt.ylabel("Products")
plt.xlabel("Sales (log scale)")

plt.legend()
plt.show()
#plt.savefig("isWordEffect.png")

A = np.array(data_a['sales'])
B = np.array(data_b['sales'])

print(stats.mannwhitneyu(A, B, alternative='two-sided'))
