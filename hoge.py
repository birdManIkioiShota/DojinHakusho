import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/raw_data.csv")
data = data[["price", "sales"]]
print(data.describe())

plt.hist(data['sales'], bins=np.logspace(1,5,30))
plt.gca().set_xscale("log")
plt.show()
