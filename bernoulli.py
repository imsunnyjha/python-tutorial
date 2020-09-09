#Use this notebook 3-fold:
    #* Play with parameters and visualize how (1 + x)^n grows compared to 1 + nx
    #* Compute how much money you will have on day n given the starting cash if you earn x% every day
    #* Determine when you will reach the specified wealth given the starting sum and the percentage you earn every day
#%%


import matplotlib.pyplot as plt
import numpy as np

# You can play with the range of values for n and with the base 1.02, see what changes
sample = 200
x = np.arange(sample)
# This is used to plot the graph of 1.02^n, it is blue on the picture below
y = 1.09 ** x
plt.plot(x, y)
plt.xlabel('n')
plt.ylabel('Money($)')
# This is used to plot the graph of 1 + 0.02 * n, it is green on the picture below
z = 1 + 0.09 * x
plt.plot(x, z)
plt.show()
# %%
