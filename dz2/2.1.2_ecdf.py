import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import nbinom

def data_ECDF(d):
    data = d.tolist()
    yList = []
    step = 0
    xList = sorted(set(data))
    dataLen = len(data)
    for elem in xList:
        count = data.count(elem)
        step += count
        yList.append(step / dataLen)
    return xList, yList

[m, p] = [5, 0.35]
N = [5, 10, 100, 1000, 10**5]
fig = plt.figure()

for n in N:
    print("n = ", n)
    for i in range(5):
        P = np.zeros(n)
        maxx = 0
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
        if np.max(P) > maxx:
            maxx = np.max(P)
        print(P)
        x, y = data_ECDF(P)
        plt.step([0, *x, 1.1 * x[-1]],[0, *y, 1],label="NB ECDF{h}".format(h=i+1), where='post')
    xx = range(maxx.astype(int))
    plt.step(xx, nbinom.cdf(xx, m, p), color='k', lw=3, label="NB CDF")
    plt.legend(loc='lower right', frameon=False)
    plt.show()
