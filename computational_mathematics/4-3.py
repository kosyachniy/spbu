# Метод Гаусса

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from fractions import Fraction
from two import solve_lin

a = 0.8
b = 1.3
alpha = 0
beta = Fraction(4, 7)
f = lambda x: 5.7 * np.cos(2.5 * x) * np.exp(-4 * x / 7) + 4.4 * np.sin(4.3 * x) * np.exp(2 * x / 7) + 5
meth = 984.121 / 6 * 0.0059963006023113501973584582773015

sc_py = integrate.quad(lambda x: f(x) * (1 / ((x - a) ** alpha * (b - x) ** beta)), 1.8, 2.3)

def solve_polynom_3(coef0, coef1, coef2):
	eps = 1e-6
	q = (coef0 * coef0 - 3 * coef1) / 9
	r = (2 * coef0 ** 3 - 9 * coef0 * coef1 + 27 * coef2) / 54
	if r * r < q ** 3:
		t = np.arccos(r / (q ** 3) ** 0.5) / 3
		return -2.0 * q ** 0.5 * np.cos(t) - coef0 / 3, -2.0 * q ** 0.5 * np.cos(t + (2 * np.pi / 3)) \
			   - coef0 / 3, -2.0 * q ** 0.5 * np.cos(t - (2 * np.pi / 3)) - coef0 / 3

	else:
		f = -r + (r * r - q ** 3) ** 0.5
		_a = np.sign(f) * abs(f) ** (1.0 / 3.0)
		if abs(_a) < eps:
			return -coef0 / 3
		else:
			B = q / _a
			x1 = (_a + B) - coef0 / 3
			x2 = -_a - coef0 / 3
			if abs(x2 * (x2 * (x2 + coef0) + coef1) + coef2) < eps:
				return x1, x2
			else:
				return x1


def iqf(start, finish):
	x1 = start
	x3 = finish
	# p(x) = 1 / ((x - a)^alpha * (b - x)^beta))

	nu0 = ((2.3 - x1) ** 0.4 - (2.3 - x3) ** 0.4) / 0.4
	nu1 = ((2.3 - x3) ** 1.4 - (2.3 - x1) ** 1.4) / 1.4 + 1 * 2.3 * nu0
	nu2 = ((2.3 - x1) ** 2.4 - (2.3 - x3) ** 2.4) / 2.4 + 2 * 2.3 * nu1 - 2.3 * 2.3 * nu0
	nu3 = ((2.3 - x3) ** 3.4 - (2.3 - x1) ** 3.4) / 3.4 + 3 * 2.3 * nu2 - 3 * 2.3 * 2.3 * nu1 + (2.3 ** 3) * nu0
	nu4 = ((2.3 - x1) ** 4.4 - (2.3 - x3) ** 4.4) / 4.4 + 4 * 2.3 * nu3 - 6 * 2.3 * 2.3 * nu2 + 4 * (2.3 ** 3) * nu1 - (
			2.3 ** 4) * nu0
	nu5 = ((2.3 - x3) ** 5.4 - (2.3 - x1) ** 5.4) / 5.4 + 5 * 2.3 * nu4 - 10 * 2.3 * 2.3 * nu3 + 10 * (
			2.3 ** 3) * nu2 - 5 * (2.3 ** 4) * nu1 + (2.3 ** 5) * nu0

	a_mat = np.array([[nu0, nu1, nu2],
					  [nu1, nu2, nu3],
					  [nu2, nu3, nu4]])
	b_vec = np.array([[-nu3], [-nu4], [-nu5]])

	tmp = solve_lin(a_mat, b_vec)
	tmp_x = solve_polynom_3(tmp[2], tmp[1], tmp[0])

	tmp__a = np.array([[1, 1, 1],
					   [tmp_x[0], tmp_x[1], tmp_x[2]],
					   [tmp_x[0] ** 2, tmp_x[1] ** 2, tmp_x[2] ** 2]])
	tmp_b = np.array([[nu0], [nu1], [nu2]])

	ans = solve_lin(tmp__a, tmp_b)

	integral = ans[0] * f(tmp_x[0]) + ans[1] * f(tmp_x[1]) + ans[2] * f(tmp_x[2])

	return integral[0]


def cqf(num_partitions):
	step_len = (b - a) / num_partitions
	sum = 0
	for i in range(num_partitions):
		sum += iqf(a + step_len * i, a + step_len * (i + 1))
	return sum


def cqf_half():
	eps = 1e-6
	multiplier = 2
	num_partitions = 1
	sum1 = cqf(num_partitions)
	sum2 = cqf(num_partitions * multiplier)
	sum3 = cqf(num_partitions * multiplier * multiplier)

	m = -np.log((sum3 - sum2) / (sum2 - sum1)) / np.log(multiplier)
	richardson = (sum3 - sum2) / (multiplier ** m - 1)
	num_partitions *= multiplier * multiplier
	while abs(richardson) > eps:
		sum1 = sum2
		sum2 = sum3
		num_partitions *= multiplier
		sum3 = cqf(num_partitions)

		m = - np.log((sum3 - sum2) / (sum2 - sum1)) / np.log(multiplier)  # convergence rate
		richardson = (sum3 - sum2) / (multiplier ** m - 1)
	return sum3 + richardson


def cqf_opt():
	eps = 1e-6
	multiplier = 2
	sum1 = cqf(1)
	sum2 = cqf(2)
	sum3 = cqf(4)
	m = 3
	richardson = (sum3 - sum2) / (multiplier ** m - 1.)

	while abs(richardson) > eps:
		h_opt = .95 * (b - a) / multiplier * ((eps * (1. - multiplier ** (-m))) / abs(sum2 - sum1)) ** (1. / m)
		num_partitions = np.ceil((b - a) / h_opt)
		sum1 = sum2
		sum2 = sum3
		sum3 = cqf(int(num_partitions))

		richardson = (sum3 - sum2) / (multiplier ** m - 1)

	return sum3 + richardson

if __name__ == '__main__':
	print('-' * 100)

	print('1: ', iqf(a, b))

	print('2: ', cqf_half())

	c_o = cqf_opt()
	print('3: ', c_o)
	print('Δ: ', abs(c_o - sc_py[0]))

	print('-' * 100)