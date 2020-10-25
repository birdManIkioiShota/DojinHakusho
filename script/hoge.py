import matplotlib.pyplot as plt
import numpy as np

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low), 0)

data = np.column_stack((data, data * 2., data + 20.))

# Add a NaN
data[30, 0] = np.NaN
data[20, 1] = np.NaN

# Filter data using np.isnan
mask = ~np.isnan(data)
filtered_data = [d[m] for d, m in zip(data.T, mask.T)]

# basic plot
print(filtered_data)
#plt.boxplot(filtered_data)
#plt.show()
