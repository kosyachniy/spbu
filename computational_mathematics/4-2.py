# Метод Ньютона-Котса

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from fractions import Fraction

a = 0.8
b = 1.3
alpha = 0
beta = Fraction(4, 7)
f = lambda x: 5.7 * np.cos(2.5 * x) * np.exp(-4 * x / 7) + 4.4 * np.sin(4.3 * x) * np.exp(2 * x / 7) + 5
meth = 984.121 / 6 * 0.0059963006023113501973584582773015

sc_py = integrate.quad(lambda x: f(x) * (1 / ((x - a) ** alpha * (b - x) ** beta)), 1.8, 2.3)
# print('SciPy: ', sc_py)
# print('WOLFRAM ALPHA: 1.18515\n')

def iqf(start, finish):
	x1 = start
	x2 = (start + finish) / 2
	x3 = finish

	nu0 = ((2.3 - x1)**0.4 - (2.3 - x3)**0.4)/0.4
	nu1 = ((2.3 - x3)**1.4 - (2.3 - x1)**1.4)/1.4 + 2.3 * nu0
	nu2 = ((2.3 - x1)**2.4 - (2.3 - x3)**2.4)/2.4 + 2 * 2.3 * nu1 - 2.3 * 2.3 * nu0

	a1 = (nu2 - nu1 * (x2 + x3) + nu0 * x2 * x3) / ((x2 - x1) * (x3 - x1))
	a2 = -(nu2 - nu1 * (x1 + x3) + nu0 * x1 * x3) / ((x2 - x1) * (x3 - x2))
	a3 = (nu2 - nu1 * (x2 + x1) + nu0 * x2 * x1) / ((x3 - x2) * (x3 - x1))

	return a1 * f(x1) + a2 * f(x2) + a3 * f(x3)

def cqf(num_partitions):
	step_len = (b - a)/num_partitions
	sum = 0
	for i in range(num_partitions):
		sum += iqf(a+step_len*i, a+step_len*(i+1))
	return sum

def cqf_half():
	eps = 1e-6
	multiplier = 2
	num_partitions = 1
	sum1 = cqf(num_partitions)
	sum2 = cqf(num_partitions * multiplier)
	sum3 = cqf(num_partitions * multiplier * multiplier)
	
	m = -np.log((sum3 - sum2) / (sum2 - sum1)) / np.log(multiplier)
	richardson = (sum3 - sum2) / (multiplier**m - 1)
	num_partitions *= multiplier * multiplier
	while abs(richardson) > eps:
		sum1 = sum2
		sum2 = sum3
		num_partitions *= multiplier
		sum3 = cqf(num_partitions)
	
		m = - np.log((sum3 - sum2) / (sum2 - sum1)) / np.log(multiplier) 
		#print(m)
		richardson = (sum3 - sum2) / (multiplier**m - 1)
	return sum3 + richardson


def cqf_opt():
	eps = 1e-6
	multiplier = 2
	sum1 = cqf(1)
	sum2 = cqf(2)
	sum3 = cqf(4)
	m = 3
	richardson = (sum3 - sum2) / (multiplier**m - 1.)

	while abs(richardson) > eps:
		h_opt = .95 * (b - a) / multiplier * ((eps * (1. - multiplier**(-m))) / abs(sum2 - sum1))**(1. / m)
		num_partitions = np.ceil((b - a) / h_opt)
		sum1 = sum2
		sum2 = sum3
		sum3 = cqf(int(num_partitions))

		richardson = (sum3 - sum2) / (multiplier**m - 1)

	return sum3 + richardson

if __name__ == '__main__':
	print('-' * 100)

	print('1:', iqf(a, b))

	print('2:', cqf_half())

	c_o = cqf_opt()
	print('3:', c_o)
	print('Δ:', abs(c_o - sc_py[0]))

	print('-' * 100)