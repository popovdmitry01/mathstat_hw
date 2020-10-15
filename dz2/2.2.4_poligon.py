import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pareto

def poligon_par(n):
  for i in range(5):
      data = np.zeros(n)
      for iteration in range(n):
          xi = np.random.rand()
          r = xm / xi ** (1 / a)
          data[iteration] = r
      data = np.around(data, decimals=2)
      unique, counts = np.unique(data, return_counts=True)
      if n > 10:
          max_value = np.amax(counts)
          print(max_value)
          plt.plot(unique, counts * 5 / max_value, label="Pareto EPMF{h}".format(h=i + 1))
      else:
          plt.plot(unique, counts, label="Pareto EPMF{h}".format(h=i + 1))
  return data

[a, xm] = [5, 1]
ddata = poligon_par(5)
plt.plot(np.unique(ddata), pareto.pdf(np.unique(ddata), a, scale=xm), color="black", lw=4, label="Pareto PMF")
plt.legend(loc='best', frameon=False)
plt.show()
ddata = poligon_par(10)
plt.plot(np.unique(ddata), pareto.pdf(np.unique(ddata), a, scale=xm), color="black", lw=4, label="Pareto PMF")
plt.legend(loc='best', frameon=False)
plt.show()
ddata = poligon_par(100)
plt.plot(np.unique(ddata), pareto.pdf(np.unique(ddata), a, scale=xm), color="black", lw=4, label="Pareto PMF")
plt.legend(loc='best', frameon=False)
plt.show()
ddata = poligon_par(1000)
plt.plot(np.unique(ddata), pareto.pdf(np.unique(ddata), a, scale=xm), color="black", lw=4, label="Pareto PMF")
plt.legend(loc='best', frameon=False)
plt.show()
ddata = poligon_par(100000)
plt.plot(np.unique(ddata), pareto.pdf(np.unique(ddata), a, scale=xm), color="black", lw=4, label="Pareto PMF")
plt.legend(loc='best', frameon=False)
plt.show()
