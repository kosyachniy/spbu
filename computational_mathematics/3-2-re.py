from scipy.optimize import fsolve
import numpy as np

x = np.array([0.5, 0.5, 1.5, -1.0, -0.5, 1.5, 0.5, -0.5, 1.5, -1.5]).T

def f(arg):
	return [
	np.cos(arg[0] * arg[1]) - np.exp(-3.0 * arg[2]) + arg[3] * arg[4] * arg[4] - arg[5] - np.sinh(2 * arg[7]) * arg[8] + 2.0 * arg[9] + 2.0004339741653854440,
	np.sin(arg[0] * arg[1]) + arg[2] * arg[8] * arg[6] - np.exp(-arg[9] + arg[5]) + 3 * arg[4] * arg[4] - arg[5] * (arg[7] + 1.0) + 10.886272036407019994,
	arg[0] - arg[1] + arg[2] - arg[3] + arg[4] - arg[5] + arg[6] - arg[7] + arg[8] - arg[9] - 3.1361904761904761904,
	2.0 * np.cos(-arg[8] + arg[3]) + arg[4] / (arg[2] + arg[0]) - np.sin(arg[1] * arg[1]) + np.cos(arg[6] * arg[9]) * np.cos(arg[6] * arg[9]) - arg[7] - 0.1707472705022304757,
	np.sin(arg[4]) + 2.0 * arg[7] * (arg[2] + arg[0]) - np.exp(-arg[6] * (-arg[9] + arg[5])) + 2.0 * np.cos(arg[1]) - 1.0 / (arg[3] - arg[8]) - 0.3685896273101277862,
	np.exp(arg[0] - arg[3] - arg[8]) + arg[4] * arg[4] / arg[7] + 0.5 * np.cos(3 * arg[9] * arg[1]) - arg[5] * arg[2] + 2.0491086016771875115,
	arg[1] * arg[1] * arg[1] * arg[6] - np.sin(arg[9] / arg[4] + arg[7]) + (arg[0] - arg[5]) * np.cos(arg[3]) + arg[2] - 0.7380430076202798014,
	arg[4] * (arg[0] - 2.0 * arg[5]) * (arg[0] - 2.0 * arg[5]) - 2.0 * np.sin(-arg[8] + arg[2]) + 1.5 * arg[3] - np.exp(arg[1] * arg[6] + arg[9]) + 3.566832198969380904,
	7.0 / arg[5] + np.exp(arg[4] + arg[3]) - 2.0 * arg[1] * arg[7] * arg[9] * arg[6] + 3.0 * arg[8] - 3.0 * arg[0] - 8.4394734508383257499,
	arg[9] * arg[0] + arg[8] * arg[1] - arg[7] * arg[2] + np.sin(arg[3] + arg[4] + arg[5]) * arg[6] - 0.78238095238095238096,
	]

xx = fsolve(f, x)

print(xx, f(xx))

# from sympy import nsolve
# print(nsolve(equations, ))