import numpy as np
from numba import vectorize


N = 100000
A = np.ones(N, dtype=np.float32)
B = np.ones(A.shape, dtype=A.dtype)
C = np.empty_like(A, dtype=A.dtype)


@vectorize(['float32(float32, float32)'], target='cuda')
def Add(a, b):
  return a + b

C = Add(A, B)