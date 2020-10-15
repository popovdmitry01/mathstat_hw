import numpy as np
[m, p] = [5, 0.35]
N = [5, 10, 10**2, 10**3, 10**5]
for n in N:
  print("n = ", n)
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
      print(P)
