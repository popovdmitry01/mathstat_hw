import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import nbinom
[m, n, p] = [5, 10**5, 0.35]
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

fig = plt.figure()
plt.hist(P, density=True, bins=30, label='NB pdf simulation')
x = np.arange(nbinom.ppf(0.01, m, p), nbinom.ppf(0.99, m, p))
plt.plot(x, nbinom.pmf(x, m, p), '-r', lw=3, label='NB pdf')
plt.legend(loc='best', frameon=False)
plt.show()
