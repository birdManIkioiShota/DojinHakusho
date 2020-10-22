import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/raw_data.csv", index_col='id')
#data = data[["price", "sales"]]
#print(data.describe())

data['date'] = pd.to_datetime(data['date'])

#print(data.describe())
data = data[['date', 'sales']]
data.set_index('date', inplace=True)
print(data.resample('Y').sum())
# sale sum

# hist
plt.hist(data['sales'], bins=np.logspace(1,5,int(np.sqrt(len(data)))))
plt.gca().set_xscale("log")
plt.show()

#print(data['circle'].value_counts())
