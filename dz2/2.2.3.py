import numpy as np
from scipy.stats import pareto

def quantile(x, y, q):
    if q <= y[0]:
        return x[0]
    else:
        for i in range(len(y) - 1):
            if y[i] <= q <= y[i+1]:
                return x[i]
        else:
            return x[len(y)-1]

def efr(data):
    yList = []
    step = 0
    xList = sorted(set(data))
    dataLen = len(data)
    for elem in xList:
        count = data.count(elem)
        step += count
        yList.append(step / dataLen)
    return xList, yList

def print_quantile(n):
    quan = [0.1, 0.5, 0.7]
    for qq in quan:
        print("level =", qq, "n =", n, end=": ")
        res = []
        for i in range(5):
            data = np.zeros(n)
            for iteration in range(n):
                xi = np.random.rand()
                r = xm / xi ** (1 / a)
                data[iteration] = r
            x, y = efr(data.tolist())
            res.append(quantile(x,y, qq))
        print(res)

[a, xm] = [5, 1]
N = [5, 10, 100, 1000, 10000]
for n in N:
    print_quantile(n)
print("Theoretical quantiles: ", np.quantile(pareto.rvs(a, scale=xm,size=10**5), [0.1, 0.5, 0.7]))
