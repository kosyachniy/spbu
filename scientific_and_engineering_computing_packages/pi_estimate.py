import numpy as np


def pi(n):
  data = np.random.rand(int(n), 2)
  circle = (data[:, 1]) ** 2 + (data[:, 0]) ** 2 < 1
  return 4 * circle.sum() / len(data)


for n in [100, 1000, 10000, 100000, 1e+6]:
  print(pi(n))
