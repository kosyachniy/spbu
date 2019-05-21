#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import time
import numpy as np
from import_file import *

e = 10e-4
n = 10

def func(arg):
    result = np.zeros((10, 1))
    result[0, 0] = np.cos(arg[0] * arg[1]) - np.exp(-3.0 * arg[2]) + arg[3] * arg[4] * arg[4] - arg[5] - np.sinh(2 * arg[7]) * arg[8] + 2.0 * arg[9] + 2.0004339741653854440
    result[1, 0] = np.sin(arg[0] * arg[1]) + arg[2] * arg[8] * arg[6] - np.exp(-arg[9] + arg[5]) + 3 * arg[4] * arg[4] - arg[5] * (arg[7] + 1.0) + 10.886272036407019994
    result[2, 0] = arg[0] - arg[1] + arg[2] - arg[3] + arg[4] - arg[5] + arg[6] - arg[7] + arg[8] - arg[9] - 3.1361904761904761904
    result[3, 0] = 2.0 * np.cos(-arg[8] + arg[3]) + arg[4] / (arg[2] + arg[0]) - np.sin(arg[1] * arg[1]) + np.cos(arg[6] * arg[9]) * np.cos(arg[6] * arg[9]) - arg[7] - 0.1707472705022304757
    result[4, 0] = np.sin(arg[4]) + 2.0 * arg[7] * (arg[2] + arg[0]) - np.exp(-arg[6] * (-arg[9] + arg[5])) + 2.0 * np.cos(arg[1]) - 1.0 / (arg[3] - arg[8]) - 0.3685896273101277862
    result[5, 0] = np.exp(arg[0] - arg[3] - arg[8]) + arg[4] * arg[4] / arg[7] + 0.5 * np.cos(3 * arg[9] * arg[1]) - arg[5] * arg[2] + 2.0491086016771875115
    result[6, 0] = arg[1] * arg[1] * arg[1] * arg[6] - np.sin(arg[9] / arg[4] + arg[7]) + (arg[0] - arg[5]) * np.cos(arg[3]) + arg[2] - 0.7380430076202798014
    result[7, 0] = arg[4] * (arg[0] - 2.0 * arg[5]) * (arg[0] - 2.0 * arg[5]) - 2.0 * np.sin(-arg[8] + arg[2]) + 1.5 * arg[3] - np.exp(arg[1] * arg[6] + arg[9]) + 3.566832198969380904
    result[8, 0] = 7.0 / arg[5] + np.exp(arg[4] + arg[3]) - 2.0 * arg[1] * arg[7] * arg[9] * arg[6] + 3.0 * arg[8] - 3.0 * arg[0] - 8.4394734508383257499
    result[9, 0] = arg[9] * arg[0] + arg[8] * arg[1] - arg[7] * arg[2] + np.sin(arg[3] + arg[4] + arg[5]) * arg[6] - 0.78238095238095238096

    return -result

def jacobian(arg):
    jac = np.zeros((10, 10))
    jac[0, 0] = -np.sin(arg[0] * arg[1]) * arg[1]
    jac[0, 1] = -np.sin(arg[0] * arg[1]) * arg[0]
    jac[0, 2] = 3.0 * np.exp(-3.0 * arg[2])
    jac[0, 3] = arg[4] * arg[4]
    jac[0, 4] = 2.0 * arg[3] * arg[4]
    jac[0, 5] = -1.0
    jac[0, 6] = 0.0
    jac[0, 7] = -2.0 * np.cosh(2 * arg[7]) * arg[8]
    jac[0, 8] = -np.sinh(2.0 * arg[7])
    jac[0, 9] = 2.0
    jac[1, 0] = np.cos(arg[0] * arg[1]) * arg[1]
    jac[1, 1] = np.cos(arg[0] * arg[1]) * arg[0]
    jac[1, 2] = arg[8] * arg[6]
    jac[1, 3] = 0.0
    jac[1, 4] = 6.0 * arg[4]
    jac[1, 5] = -np.exp(-arg[9] + arg[5]) - arg[7] - 1.0
    jac[1, 6] = arg[2] * arg[8]
    jac[1, 7] = -arg[5]
    jac[1, 8] = arg[2] * arg[6]
    jac[1, 9] = np.exp(-arg[9] + arg[5])
    jac[2, 0] = 1.0
    jac[2, 1] = -1.0
    jac[2, 2] = 1.0
    jac[2, 3] = -1.0
    jac[2, 4] = 1.0
    jac[2, 5] = -1.0
    jac[2, 6] = 1.0
    jac[2, 7] = -1.0
    jac[2, 8] = 1.0
    jac[2, 9] = -1.0
    jac[3, 0] = -arg[4] * (arg[2] + arg[0])**(-2.0)
    jac[3, 1] = -2.0 * np.cos(arg[1] * arg[1]) * arg[1]
    jac[3, 2] = -arg[4] * (arg[2] + arg[0])**(-2.0)
    jac[3, 3] = -2.0 * np.sin(-arg[8] + arg[3])
    jac[3, 4] = 1.0 / (arg[2] + arg[0])
    jac[3, 5] = 0.0
    jac[3, 6] = -2.0 * np.cos(arg[6] * arg[9]) * np.sin(arg[6] * arg[9]) * arg[9]
    jac[3, 7] = -1.0
    jac[3, 8] = 2.0 * np.sin(-arg[8] + arg[3])
    jac[3, 9] = -2.0 * np.cos(arg[6] * arg[9]) * np.sin(arg[6] * arg[9]) * arg[6]
    jac[4, 0] = 2.0 * arg[7]
    jac[4, 1] = -2.0 * np.sin(arg[1])
    jac[4, 2] = 2.0 * arg[7]
    jac[4, 3] = (-arg[8] + arg[3])**(-2.0)
    jac[4, 4] = np.cos(arg[4])
    jac[4, 5] = arg[6] * np.exp(-arg[6] * (-arg[9] + arg[5]))
    jac[4, 6] = -(arg[9] - arg[5]) * np.exp(-arg[6] * (-arg[9] + arg[5]))
    jac[4, 7] = 2.0 * arg[2] + 2.0 * arg[0]
    jac[4, 8] = -(-arg[8] + arg[3])**(-2.)
    jac[4, 9] = -arg[6] * np.exp(-arg[6] * (-arg[9] + arg[5]))
    jac[5, 0] = np.exp(arg[0] - arg[3] - arg[8])
    jac[5, 1] = -1.5 * np.sin(3. * arg[9] * arg[1]) * arg[9]
    jac[5, 2] = -arg[5]
    jac[5, 3] = -np.exp(arg[0] - arg[3] - arg[8])
    jac[5, 4] = 2.0 * arg[4] / arg[7]
    jac[5, 5] = -arg[2]
    jac[5, 6] = 0.0
    jac[5, 7] = -arg[4] * arg[4] * (arg[7])**(-2.)
    jac[5, 8] = -np.exp(arg[0] - arg[3] - arg[8])
    jac[5, 9] = -1.5 * np.sin(3. * arg[9] * arg[1]) * arg[1]
    jac[6, 0] = np.cos(arg[3])
    jac[6, 1] = 3.0 * arg[1] * arg[1] * arg[6]
    jac[6, 2] = 1.0
    jac[6, 3] = -(arg[0] - arg[5]) * np.sin(arg[3])
    jac[6, 4] = np.cos(arg[9] / arg[4] + arg[7]) * arg[9] * (arg[4])**(-2.0)
    jac[6, 5] = -np.cos(arg[3])
    jac[6, 6] = (arg[1])**3.
    jac[6, 7] = -np.cos(arg[9] / arg[4] + arg[7])
    jac[6, 8] = 0.0
    jac[6, 9] = -np.cos(arg[9] / arg[4] + arg[7]) / arg[4]
    jac[7, 0] = 2.0 * arg[4] * (arg[0] - 2. * arg[5])
    jac[7, 1] = -arg[6] * np.exp(arg[1] * arg[6] + arg[9])
    jac[7, 2] = -2.0 * np.cos(-arg[8] + arg[2])
    jac[7, 3] = 1.5
    jac[7, 4] = (arg[0] - 2. * arg[5])**2.0
    jac[7, 5] = -4.0 * arg[4] * (arg[0] - 2.0 * arg[5])
    jac[7, 6] = -arg[1] * np.exp((arg[1] * arg[6]) + arg[9])
    jac[7, 7] = 0.0
    jac[7, 8] = 2.0 * np.cos(-arg[8] + arg[2])
    jac[7, 9] = -np.exp((arg[1] * arg[6]) + arg[9])
    jac[8, 0] = -3.0
    jac[8, 1] = -2.0 * arg[7] * arg[9] * arg[6]
    jac[8, 2] = 0.0
    jac[8, 3] = np.exp((arg[4] + arg[3]))
    jac[8, 4] = np.exp((arg[4] + arg[3]))
    jac[8, 5] = -7.0 * (arg[5])**(-2.0)
    jac[8, 6] = -2.0 * arg[1] * arg[7] * arg[9]
    jac[8, 7] = -2.0 * arg[1] * arg[9] * arg[6]
    jac[8, 8] = 3.0
    jac[8, 9] = -2.0 * arg[1] * arg[7] * arg[6]
    jac[9, 0] = arg[9]
    jac[9, 1] = arg[8]
    jac[9, 2] = -arg[7]
    jac[9, 3] = np.cos(arg[3] + arg[4] + arg[5]) * arg[6]
    jac[9, 4] = np.cos(arg[3] + arg[4] + arg[5]) * arg[6]
    jac[9, 5] = np.cos(arg[3] + arg[4] + arg[5]) * arg[6]
    jac[9, 6] = np.sin(arg[3] + arg[4] + arg[5])
    jac[9, 7] = -arg[2]
    jac[9, 8] = arg[1]
    jac[9, 9] = arg[0]

    return jac


def solve_lin_eq(a, b):
    p, l, u, q, rank, t = decompose(a)

    rows, cols = a.shape
    y = np.zeros(rows)

    b = np.dot(p, b)

    y[0] = b[0]

    for i in range(1, rows):
        sum = 0
        for j in range(i):
            sum += y[j] * l[i, j]
        y[i] = b[i] - sum

    x = np.zeros((rows, 1))

    for j in range(rows-1, 0, -1):
        if np.allclose(u[j], x, atol=10e-9) and abs(y[j]) < 10e-9:
            rows -= 1
            cols -= 1
        elif np.allclose(u[j], x, atol=10e-9) and not abs(y[j]) < 10e-9:
            print("Isn't consistent!")
            return x

    x[rows-1, 0] = y[rows-1] / u[rows-1, cols-1]

    for i in range(2, rows+1):
        sum = 0
        for j in range(1, i):
            sum += x[rows-j, 0] * u[rows-i, cols-j]
        x[rows-i, 0] = (y[rows-i] - sum) / u[rows-i, rows-i]
    x = np.dot(q, x)
    return x


def solve_lin_eq_wd(p, l, u, q, b):
    rows, cols = p.shape

    y = np.zeros(rows)

    b = np.dot(p, b)

    y[0] = b[0]

    for i in range(1, rows):
        sum = 0
        for j in range(i):
            sum += y[j] * l[i, j]
        y[i] = b[i] - sum

    x = np.zeros((rows, 1))

    for j in range(rows-1, 0, -1):
        if np.allclose(u[j], x, atol=10e-9) and abs(y[j]) < 10e-9:
            rows -= 1
            cols -= 1
        elif np.allclose(u[j], x, atol=10e-9) and not abs(y[j]) < 10e-9:
            print("Isn't consistent!")
            return x

    x[rows-1, 0] = y[rows-1] / u[rows-1, cols-1]

    for i in range(2, rows+1):
        sum = 0
        for j in range(1, i):
            sum += x[rows-j, 0] * u[rows-i, cols-j]
        x[rows-i, 0] = (y[rows-i] - sum) / u[rows-i, rows-i]
    x = np.dot(q, x)
    return x




def newton(x_orig):
    x_start = np.copy(x_orig)
    max_iterations = 1e3
    iter_count = 0
    operations_count = 0
    start_time = time.clock()
    n = 10
    while True:
        f = func(x_start)
        operations_count += n
        j = jacobian(x_start)
        operations_count += n * n

        delta = solve_lin_eq(j, f)
        operations_count += 2 * n**3
        x_start += delta

        iter_count += 1

        if abs(delta).max() < 1e-6 or iter_count > max_iterations:
            break

    print("Итераций:")
    print(iter_count)
    print("Время: секунд")
    print(time.clock() - start_time)
    print("Операций:")
    print(operations_count)
    print(x_start.T)
    print(func(x_start).T)


def newton_mod(x_orig):
    x_start = np.copy(x_orig)

    max_iterations = 1e3
    iter_count = 0
    start_time = time.clock()
    operations_count = 0
    n = 10

    j = jacobian(x_start)
    operations_count += n * n

    p, l, u, q, _, _ = decompose(j)
    operations_count += 2 * n ** 3

    while True:
        f = func(x_start)
        operations_count += n

        delta = solve_lin_eq_wd(p, l, u, q, f)
        operations_count += n * n

        x_start += delta

        iter_count += 1

        if abs(delta).max() < 1e-6 or iter_count > max_iterations:
            break

    print("Итераций:")
    print(iter_count)
    print("Время: секунд")
    print(time.clock() - start_time)
    print("Операций:")
    print(operations_count)
    print(x_start.T)
    print(func(x_start).T)


def auto_modif_newton(x_orig, k):
    x_start = np.copy(x_orig)

    max_iterations = 1e3
    iter_count = 0
    start_time = time.clock()

    n = 10
    operations_count = 0

    while True:
        f = func(x_start)
        operations_count += n

        j = jacobian(x_start)
        operations_count += n * n

        delta = solve_lin_eq(j, f)
        operations_count += 2 * n ** 3

        x_start += delta

        iter_count += 1

        if abs(delta).max() < 1e-6 or iter_count > max_iterations:
            break

        if iter_count >= k:
            p, l, u, q, _, _ = decompose(j)
            operations_count += 2 * n ** 3

            while True:
                f = func(x_start)
                operations_count += n

                delta = solve_lin_eq_wd(p, l, u, q, f)
                operations_count += n * n

                x_start += delta

                iter_count += 1

                if abs(delta).max() < 1e-6 or iter_count > max_iterations:
                    break

        if abs(delta).max() < 1e-6 or iter_count > max_iterations:
            break

    print("Итераций:")
    print(iter_count)
    print("Время: секунд")
    print(time.clock() - start_time)
    print("Операций:")
    print(operations_count)
    print(x_start.T)
    print(func(x_start).T)


def hybrid_newton(x_orig, k):
    x_start = np.copy(x_orig)

    max_iterations = 1e3
    iter_count = 0
    start_time = time.clock()
    operations_count = 0
    n = 10

    while True:
        if k == 0 or iter_count % k == 0:
            j = jacobian(x_start)
            operations_count += n * n
            p, l, u, q, _, _ = decompose(j)
            operations_count += 2 * n ** 3 

        f = func(x_start)
        operations_count += n

        delta = solve_lin_eq_wd(p, l, u, q, f)
        operations_count += n * n

        x_start += delta

        iter_count += 1

        if abs(delta).max() < 1e-6 or iter_count > max_iterations:
            break

    print("Итераций:")
    print(iter_count)
    print("Время:секунд")
    print(time.clock() - start_time)
    print("Операций:")
    print(operations_count)
    print(x_start.T)
    print(func(x_start).T)


if __name__ == '__main__':
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

    x = np.array([[0.5], [0.5], [1.5], [-1.0], [-0.5], [1.5], [0.5], [-0.5], [1.5], [-1.5]])


    print("Метод Ньютона:")
    newton(x)
    print("\n")

    print("Модифицированный метод Ньютона:")
    newton_mod(x)
    print("\n")

    for i in range(1, 8, 2):
        print("С переходом на модифицированный метод на итерации:")
        print(i)
        auto_modif_newton(x, i)
        print("\n")

    for i in range(2, 8, 2):
        print("Гибридный метод, где матрица пересчитывается каждые итераций:")
        print(i)
        hybrid_newton(x, i)
        print("\n")