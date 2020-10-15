import numpy as np
from scipy.stats import nbinom

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
          x, y = efr(P.tolist())
          res.append(int(quantile(x, y, qq)))
      print(res)

[m, p] = [5, 0.35]
N = [5, 10, 100, 1000, 10**5]
for n in N:
  print_quantile(n)
print("Theoretical quantiles: ", np.quantile(nbinom.rvs(m, p, size=10**5), [0.1, 0.5, 0.7]))
