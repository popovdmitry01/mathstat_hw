import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pareto

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

[a, xm] = [5, 1]
N = [5, 10, 100, 1000, 10**5]

for n in N:
    print("n = ", n)
    for i in range(5):
        data = np.zeros(n)
        for iteration in range(n):
            xi = np.random.rand()
            r = xm / xi ** (1 / a)
            data[iteration] = r
        print(data)
        x, y = data_ECDF(data)
        plt.step([0, *x, 1.1 * x[-1]], [0, *y, 1], label="Pareto ECDF{h}".format(h=i + 1), where='post')
    xx = np.arange(0, 5, 0.1)
    plt.plot(xx, pareto.cdf(xx, a, scale=xm),color="black", label="Pareto CDF")
    plt.legend(loc='lower right', frameon=False)
    plt.show()
