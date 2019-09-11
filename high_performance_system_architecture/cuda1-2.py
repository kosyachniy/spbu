import numpy as np
from numba import cuda, float32, int32


N = 1000
NV = 300000
threadsperblock = 256

@cuda.jit('void(float32[:,:], float32[:])')
def vec_sum_row(vecs, sums):
    sm = cuda.shared.array(threadsperblock, float32)
    bid, tid, bdim = cuda.blockIdx.x, cuda.threadIdx.x, cuda.blockDim.x
    lid = tid
    sm[lid] = 0

    while lid < N:
        sm[tid] += vecs[bid, lid]
        lid += bdim

    cuda.syncthreads()
    sweep = bdim // 2

    while sweep > 0:
        if tid < sweep:
            sm[tid] += sm[tid + sweep]

        sweep = sweep // 2
        cuda.syncthreads()

    if tid == 0:
        sums[bid] = sm[0]

@cuda.jit('void(float32[:,:], float32[:])')
def vec_sum_col(vecs, sums):
    idx = cuda.grid(1)
    if idx >= NV:
        return
    temp = 0

    for i in range(N):
        temp += vecs[i,idx]

    sums[idx] = temp

rvecs = np.ones((NV, N), dtype=np.float32)
sums = np.zeros(NV, dtype=np.float32)
d_rvecs = cuda.to_device(rvecs)
d_sums = cuda.device_array_like(sums)
vec_sum_row[NV, threadsperblock](d_rvecs, d_sums)
d_sums.copy_to_host(sums)

print(sums[:8])

cvecs = np.ones((N, NV), dtype=np.float32)
d_cvecs = cuda.to_device(cvecs)
vec_sum_col[(NV + threadsperblock - 1) // threadsperblock, threadsperblock](d_cvecs, d_sums)
d_sums.copy_to_host(sums)

print(sums[:8])