# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import collections

data = pd.read_csv("../data/raw_data.csv", index_col='id')
data['date'] = pd.to_datetime(data['date'])

# 売上と値段の関係をプロットします
x = data['price']
y = data['sales']

plt.scatter(x,y,label='data')
plt.title('Relationship between Price and Sales')
plt.ylabel('Sales')
plt.xlabel('Price')

plt.grid(linestyle='dashed')
plt.savefig("../fig/getPriceSalesPlot.png")
print("Generate ../fig/getPriceSalesPlot.png")
