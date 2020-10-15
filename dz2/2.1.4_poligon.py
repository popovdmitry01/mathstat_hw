import numpy as np
from scipy.stats import nbinom
import matplotlib.pyplot as plt


fig = plt.figure()


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
        plt.plot(unique, counts/n, label="NB EPMF{h}".format(h=i+1))
    plt.plot(np.unique(P), nbinom(m, p).pmf(np.unique(P)), color='m', lw=5, label="NB PMF")
    plt.legend(loc='best')
    plt.show()
