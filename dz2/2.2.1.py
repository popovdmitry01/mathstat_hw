import numpy as np

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
