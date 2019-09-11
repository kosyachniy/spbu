import numpy as np
from numba import cuda
import timeit


TPB = 16
@cuda.jit
def matmul(A, B, C):
    sA = cuda.shared.array(shape=(TPB, TPB), dtype=float32)
    sB = cuda.shared.array(shape=(TPB, TPB), dtype=float32)

    x, y = cuda.grid(2)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    bpg = cuda.gridDim.x

    if x >= C.shape[0] and y >= C.shape[1]:
        return
    tmp = 0.
    for i in range(bpg):
        sA[tx, ty] = A[x, ty + i * TPB]
        sB[tx, ty] = B[tx + i * TPB, y]
        cuda.syncthreads()
        for j in range(TPB):
            tmp += sA[tx, j] * sB[j, ty]
        cuda.syncthreads()
    C[x, y] = tmp

N = 500
A = np.random.rand(N,N)
B = np.random.rand(N,N)

np_loop = 300
np_matmul = np.empty(np_loop)

for i in range(np_loop):
    t_start = timeit.default_timer()
    out = np.matmul(A, B)
    t_end = timeit.default_timer()
    np_matmul[i] = t_end - t_start


record = np_matmul
print ('np.matmul(A, B) выполняется в среднем {:.5f} секунд (кроме первого цикла)'.format(np_matmul[1:].mean()))

print('mean = {:.5f}'.format(record.mean()))
print('max = {:.5f}'.format(record.max()))
print('min = {:.5f}'.format(record.max()))
print('σ = {:.5f}'.format(record.std()))

print('-' * 100)
print (record)