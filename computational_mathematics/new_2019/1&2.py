#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import numpy as np
import scipy
import scipy.linalg
import random

def LU_decomposition(matrix): # LU декомпозиция
    n, m = matrix.shape
    P = np.identity(n) # единичная матрица
    L = np.identity(n)
    U = matrix.copy()
    PF = np.identity(n)
    LF = np.zeros((n,n))
    for k in range(0, n - 1):
        index = np.argmax(abs(U[k:,k]))
        index = index + k 
        if index != k:
            P = np.identity(n)
            P[[index,k],k:n] = P[[k,index],k:n]
            U[[index,k],k:n] = U[[k,index],k:n] 
            PF = np.dot(P,PF) # скалярное произведение
            LF = np.dot(P,LF)
        L = np.identity(n)
        for j in range(k+1,n):
            L[j,k] = -(U[j,k] / U[k,k])
            LF[j,k] = (U[j,k] / U[k,k])
        U = np.dot(L,U)
    np.fill_diagonal(LF, 1)
    return PF, LF, U

def determinant(A): # определитель
    n = len(A)
    d = 1.0
    P1, L1, U1 = LU_decomposition(A)
    for i in range(n):
        d = d * U1[i][i]
    return d

def LU_solver(l,u,b,P1):
    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)
    b_s = np.dot(P1,b)
    for i in range(n):
        y[i] = (b_s[i] - sum(L1[i][p] * y[p] for p in range(n)))
    for i in range(n):
        x[n-i-1] = float(y[n-i-1]-sum(U1[n-i-1][n-p-1]* x[n-p-1] for p in range(n)))/U1[n-i-1][n-i-1]
    return x

def inverse(l,u,p): # обратная матрица
    n = len(l)
    E = np.identity(n)
    
    matrix = []
   
    for i in range (n):
        b = []
        for j in range (n):
            b.append(E[i][j])
        
        stolb = LU_solver(l,u,b,p)
        matrix.append(stolb.tolist())
    matrix = np.transpose(matrix)
    return matrix

def condition_number(a,a1): # число обусловленности
    num = np.linalg.norm(a) * np.linalg.norm(a1)
    return(num)

# ##-2-##

def generate_diagonal_dominant():
    dim = random.randint(2, 10)
    matrix = 200 * np.random.rand(dim, dim) - 100
    vector = 200 * np.random.rand(dim, 1) - 100

    for i in range(dim):
        max_in_row = 0
        num_max = 0
        for j in range(dim):
            if abs(matrix[i, j]) > max_in_row:
                max_in_row = abs(matrix[i, j])
                num_max = j
        matrix[i, i], matrix[i, num_max] = matrix[i, num_max], matrix[i, i]
    for i in range(dim):
        for j in range(dim):
            if not i == j:
                matrix[i, j] /= dim-1
    return matrix, vector

def generate_positive_definite():
    dim = random.randint(2, 5)
    matrix = 200 * np.random.rand(dim, dim) - 100
    vector = 200 * np.random.rand(dim, 1) - 100
    return np.dot(matrix, matrix.T)/1000, vector

def norm_oo(a):
    norm = 0.
    rows, cols = a.shape
    for i in range(rows):
        tmp = abs(a[i]).sum()
        if tmp > norm:
            norm = tmp
    return norm

def jacobi(a, b):
    currency = 10e-12
    max_iterations = 10e3
    rows, cols = a.shape
    h = np.zeros((rows, cols))
    g = np.zeros((rows, 1))
    for i in range(rows):
        for j in range(i):
            h[i, j] = - a[i, j] / a[i, i]
        h[i, i] = 0
        for j in range(i+1, cols):
            h[i, j] = - a[i, j] / a[i, i]
        g[i, 0] = b[i, 0] / a[i, i]
    x_n_1 = np.copy(g)
    counter = 0
    koef = norm_oo(h) / (1 - norm_oo(h))
    if koef < 0:
        koef = 10
    while True:
        x_n = np.dot(h, x_n_1) + g
        x_n, x_n_1 = x_n_1, x_n
        counter += 1
        if not((koef * abs(norm_oo(x_n_1 - x_n))) > currency and counter < max_iterations):
            break
    print('Якоби:')
    print(counter)
    if counter > max_iterations or np.isnan(x_n_1[0, 0]):
        raise Exception('error')
    print(x_n_1)    
    return x_n_1

def seidel(a, b):
    currency = 10e-12
    rows, cols = a.shape
    x_n_1 = np.ones((rows, 1))
    x_n = np.zeros((rows, 1))

    counter = 0

    r = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(i, rows):
            r[i, j] = -a[i, j] / a[i, i]

    h = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            h[i, j] = -a[i, j] / a[i, i]

    print(norm_oo(h))
    koef = abs(norm_oo(r) / (1 - norm_oo(h)))
    print(koef)

    while True:
        for i in range(rows):
            x_n[i, 0] = b[i, 0] / a[i, i]
            for j in range(i):
                x_n[i, 0] -= x_n[j, 0] * a[i, j] / a[i, i]
            for j in range(i+1, rows):
                x_n[i, 0] -= x_n_1[j, 0] * a[i, j] / a[i, i]

        x_n, x_n_1 = x_n_1, x_n
        counter += 1
        # print(x_n)
        if (koef * abs(norm_oo(x_n_1 - x_n))) < currency:
            break

    print('Зейдель:')
    print(counter)
    print(x_n_1)
    return x_n_1


# MAIN

if __name__ == '__main__':

    A = np.genfromtxt('matrix.csv', delimiter=',') # считывание из файла

    print('-' * 10, 'Input', '-' * 10)

    A = np.array(A)
    P1, L1, U1 = LU_decomposition(A)
    print('A:')
    print(A)
    print('P1:')
    print(P1)
    print('L1:')
    print(L1)
    print('U1:')
    print(U1)
    # P2, L2, U2 = scipy.linalg.lu(A) # проверка
    # print(P2)
    # print(L2)
    # print(U2)


    print('-' * 10, '#1', '-' * 10)

    d = determinant(A) 
    print('Определитель:')
    print(d)

    print('-' * 10, '#2', '-' * 10)

    b = np.array([1,6,4]) # вводим b
    x = LU_solver(L1,U1,b,P1)
    print ("Решение системы. x=")
    print (x)
    print(np.allclose(np.dot(A, x), b)) # проверка

    print('-' * 10, '#3', '-' * 10)

    A_1 = inverse(L1,U1,P1)
    print("Обратная матрица:")
    print(A_1)
    print(np.linalg.inv(A)) #проверка


    print('-' * 10, '#4', '-' * 10)

    print("Число обусловленности:")
    print(condition_number(A,A_1))
    print(np.linalg.cond(A, 'fro')) #проверка

    print('-' * 10, 'End', '-' * 10)
    print('-' * 10, '## 2 ##', '-' * 10)
    mat_pd, vec_pd = generate_positive_definite()

    print('A:')
    print(mat_pd)
    print('b:')
    print(vec_pd.T)
    krya=jacobi(mat_pd,vec_pd)
    x_s_pd = seidel(mat_pd, vec_pd)
    print('Сравнение с положительно определённой матрицей:')
    print(np.dot(mat_pd, x_s_pd) - vec_pd)