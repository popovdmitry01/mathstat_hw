from scipy.stats import nbinom
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()
[m, p] = [5, 0.35]
N = [5, 10, 100, 1000, 10**5]
for n in N:
    for i in range(5):
        P = np.zeros(n)
        for iteration in range(n):
            p_it = 0
            counter = 0
            while counter < m:
                xi = np.random.rand()
                if xi <= p:
                    counter += 1
                else:
                    p_it += 1
            P[iteration] = p_it
        unique, counts = np.unique(P, return_counts=True)
        ax.hist(unique, bins=int(len(unique)), weights=counts/n, label="NB EHMF{h}".format(h=i+1), alpha=0.7)
    plt.plot(np.unique(P), nbinom(m, p).pmf(np.unique(P)), '-.',color='black', lw=2, label="NB PMF", )
    plt.legend(loc='best')
    plt.show()
