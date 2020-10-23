# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

data = pd.read_csv("../data/raw_data.csv", index_col='id')
data['date'] = pd.to_datetime(data['date'])

plt.rcParams['axes.axisbelow'] = True
plt.grid(linestyle='dashed')
plt.hist(data['sales'], bins=int(np.sqrt(len(data))), ec='black')
plt.savefig("../fig/Histogram.png")

plt.title("Sales histogram")
plt.ylabel("Number of products")
plt.xlabel("Number of sales with log scale")

plt.close()

plt.rcParams['axes.axisbelow'] = True
plt.grid(linestyle='dashed')
plt.hist(data['sales'], bins=np.logspace(1,5,int(np.sqrt(len(data)))), ec='black')
plt.gca().set_xscale("log")

plt.title("Sales histogram (log scale)")
plt.ylabel("Number of products")
plt.xlabel("Number of sales with log scale")

plt.savefig("../fig/Histogram_log.png")
