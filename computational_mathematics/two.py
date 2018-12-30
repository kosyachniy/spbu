import numpy as np
import random

def determinant(u, transp):
	rows, cols = u.shape
	det = 1.
	for i in range(rows):
		det *= u[i, i]
	if transp:
		return -det
	else:
		return det

def swap_rows(m, s, f):
	tmp = np.copy(m[f, :])
	m[f, :] = np.copy(m[s, :])
	m[s, :] = tmp

def swap_cols(m, s, f):
	tmp = np.copy(m[:, f])
	m[:, f] = np.copy(m[:, s])
	m[:, s] = tmp

def decompose(a_orig):
	transpose = False
	a = np.copy(a_orig)
	rows, cols = a.shape
	p = np.eye(rows, cols)
	q = np.eye(rows, cols)

	rank = rows
	for k in range(rows):
		pivot_value = 0

		for i in range(k, rows):
			for j in range(k, cols):
				if abs(a[i, j]) > pivot_value:
					pivot_value = abs(a[i, j])
					row_with_max_elem = i
					col_with_max_elem = j

		if pivot_value < 10e-16:
			rank -= 1
			continue

		swap_rows(a, k, row_with_max_elem)
		swap_cols(a, k, col_with_max_elem)

		if row_with_max_elem != k:
			transpose = not transpose
		if col_with_max_elem != k:
			transpose = not transpose

		swap_rows(p, k, row_with_max_elem)
		swap_cols(q, k, col_with_max_elem)

		for i in range(k + 1, rows):
			a[i, k] /= a[k, k]
			for j in range(k + 1, cols):
				a[i, j] -= a[i, k] * a[k, j]

	lower = np.eye(rows, cols)
	upper = np.zeros((rows, cols))

	for i in range(rows):
		for j in range(cols):
			if i > j:
				lower[i, j] = a[i, j]
			else:
				upper[i, j] = a[i, j]

	return p, lower, upper, q, rank, transpose

def solve_lin(a, b, dec=None):
	p, l, u, q, rank, t = dec if dec else decompose(a)

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
			print('Isn\'t consistent!')
			return x

	x[rows-1, 0] = y[rows-1] / u[rows-1, cols-1]

	for i in range(2, rows+1):
		sum = 0
		for j in range(1, i):
			sum += x[rows-j, 0] * u[rows-i, cols-j]
		x[rows-i, 0] = (y[rows-i] - sum) / u[rows-i, rows-i]
	x = np.dot(q, x)
	return x

def check_lin(a, x, b):
	dim, _ = a.shape
	ax = np.dot(a, x)
	res = np.zeros((dim, 1))
	z = np.zeros((dim, 1))
	for i in range(dim):
		res[i] = ax[i, 0] - b[i, 0]

	return np.allclose(z, res, atol=10e-9)

def inverse(a):
	rows, cols = a.shape

	inv = np.zeros((rows, cols))
	for i in range(rows):
		z = np.zeros((rows, 1))
		z[i, 0] = 1
		s = solve_lin(a, z)

		for j in range(rows):
			inv[j, i] = s[j]
	return inv

def check_inv(a, inv):
	eye = np.dot(a, inv)
	rows, cols = a.shape
	return np.allclose(eye, np.eye(rows, cols), atol=10e-9)

def inverse(a):
	rows, cols = a.shape

	inv = np.zeros((rows, cols))
	for i in range(rows):
		z = np.zeros((rows, 1))
		z[i, 0] = 1
		s = solve_lin(a, z)

		for j in range(rows):
			inv[j, i] = s[j]
	return inv

def norm(a):
	rows, cols = a.shape
	sums = np.zeros((rows, 1))

	for i in range(rows):
		sums[i, 0] = np.sum(a[i])

	return np.max(sums)

def conditional_number(a):
	inv = inverse(a)
	return norm(a) * norm(inv)


def decompose_qr(a_orig):
	r = np.copy(a_orig)
	rows, cols = r.shape
	q = np.eye(rows, cols)
	mid_mat = np.eye(rows, cols)

	for start in range(rows):
		for j in range(1, rows - start):
			if (abs(r[start, start]) > 10e-9) or (abs(r[start+j, start]) > 10e-9):
				norm = (r[start, start]**2 + r[start+j, start]**2)**0.5
				normalized_first = r[start, start] / norm
				normalized_second = r[start+j, start] / norm

				mid_mat[start, start] = normalized_first
				mid_mat[start, start+j] = normalized_second
				mid_mat[start+j, start] = -normalized_second
				mid_mat[start+j, start+j] = normalized_first

				q = np.dot(mid_mat, q)
				r = np.dot(mid_mat, r)

				mid_mat[start, start] = 1
				mid_mat[start, start + j] = 0
				mid_mat[start + j, start] = 0
				mid_mat[start + j, start + j] = 1
		mid_mat[start, start] = 1

	return q, r


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
	print('Jacobi iterations: ', counter)
	if counter > max_iterations or np.isnan(x_n_1[0, 0]):
		raise Exception('DOESN\'T COVERAGE!!!')
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
		if (koef * abs(norm_oo(x_n_1 - x_n))) < currency:
			break

	print('Seidel iterations: ', counter)
	return x_n_1


if __name__ == '__main__':
	print('\n' * 3)

	mat = np.genfromtxt('matrix.csv', delimiter=',')
	print(mat)

	print('\n', '-' * 100, '-' * 100, '№1', '-' * 100, '-' * 100, sep='\n')

	dec = decompose(mat)
	for i, x in enumerate(dec[:-1]):
		print(('P', 'L', 'U', 'Q', 'Ранг')[i], ': ', x, sep='')

	#print(*dec, sep='\n')

	print('Определитель:', determinant(mat, dec[-1]))
	print('-'*100)

	b = np.array([list(map(int, input().split())),]).reshape(mat.shape[0], -1)
	x = solve_lin(mat, b, dec)
	print('Решение СЛАУ:', x)
	print('Проверка:', check_lin(mat, x, b))
	print('-'*100)

	invm = inverse(mat)
	print('A^-1:', invm)
	print('Проверка:', check_inv(mat, invm))
	print('-' * 100)

	print('Число обусловленности:', conditional_number(mat))

	print('\n', '-' * 100, '-' * 100, '№2', '-' * 100, '-' * 100, sep='\n')

	q, r = decompose_qr(mat)
	print('Q:', q)
	print('R:', r)

	print('\n', '-' * 100, '-' * 100, '№3', '-' * 100, '-' * 100, sep='\n')

	mat_pd, vec_pd = generate_positive_definite()

	print('A:', mat_pd)
	print('b:', vec_pd.T)

	x_s_pd = seidel(mat_pd, vec_pd)
	print('Сравнение с положительно определённой матрицей:', np.dot(mat_pd, x_s_pd) - vec_pd)