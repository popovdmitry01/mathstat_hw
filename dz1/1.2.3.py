import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from scipy.stats import pareto
  
[a, xm] = [5, 1]
n = 1000
  
data = np.zeros(n)
for iteration in range(n):
    xi = np.random.rand()
    r = xm / xi**(1/a)
    data[iteration] = r

mi = np.amin(data)
ma = np.amax(data)
arr_x = list()
step = (ma - mi) / sqrt(n)
beg = round(mi, 3)
arr_x.append(beg)
for i in range(round(sqrt(n))):
    beg += step
    arr_x.append(round(beg, 3))
arr_y = list()
for j in range(round(sqrt(n))):
    count = 0
    for element in data:
        if arr_x[j] <= element and element <= arr_x[j+1]:
            count += 1
    arr_y.append(count)
arr_x.pop()
maximum = max(arr_y)
arrr_y = list()
for each in arr_y:
    el = each * a / maximum
    arrr_y.append(el)
x = np.linspace(0, 5, 1000)
par_arr = np.array(pareto.pdf(x, scale=xm, b=a))
fig = plt.figure()
ax = fig.add_subplot()
plt.hist(arr_x, weights=arrr_y, bins=round(sqrt(n)), label="Pareto pdf simulation")
plt.plot(x, par_arr, color="r", label="Pareto pdf")
plt.legend(loc='best', frameon=False)
plt.show()
