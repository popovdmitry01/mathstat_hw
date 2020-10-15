import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pareto

[a, xm] = [5, 1]
N = [5, 10, 100, 1000, 10**5]

fig = plt.figure()
ax = fig.add_subplot()

for n in N:
    for i in range(5):
        data = np.zeros(n)
        for iteration in range(n):
            xi = np.random.rand()
            r = xm / xi ** (1 / a)
            data[iteration] = r
        data = np.around(data, decimals=2)
        unique, counts = np.unique(data, return_counts=True)
        ax.hist(unique, bins=int(len(unique)), weights=counts, label="Pareto EHMF{h}".format(h=i + 1), alpha=0.7, density=True)
    plt.plot(np.unique(data), pareto.pdf(np.unique(data), a, scale=xm), '-.', color="black", lw=1, label="Pareto PMF")
    plt.legend(loc='best')
    plt.show()
