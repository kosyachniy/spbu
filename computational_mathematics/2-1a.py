import numpy as np

def determinant(u):
    rows, cols = u.shape
    det = 1.
    for i in range(rows):
        det *= u[i, i]
    if rows % 2 and rows > 2:
        det *= -1
    
    return det

if __name__ == '__main__':
    mat = np.genfromtxt('matrix.csv', delimiter=',')
    print(determinant(mat))
