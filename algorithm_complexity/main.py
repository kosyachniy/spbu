import time

import numpy as np
import matplotlib.pyplot as plt

from lsd import radixSort


def gen_digit(length, top):
	return np.random.randint(top, size=length)

def measure(length, top):
	raw = gen_digit(length, top)

	time_start = time.time()
	res = radixSort(raw)
	time_stop = time.time()

	return raw, res, time_stop - time_start

def graph():
	def timed(length_count, top_dim):
		return np.mean([measure(length_count, 10 ** top_dim)[2] for i in range(10)])
	
	timed_top = lambda dimension: timed(int(10e1), dimension)
	top_x = np.arange(1, 10)
	top_y = [i * 1000 for i in map(timed_top, top_x)]
	
	timed_length = lambda count: timed(count, 3)
	length_x = [int(i) for i in np.arange(10e2, 10e3, step=10e2)]
	length_y = [i * 1000 for i in map(timed_length, length_x)]

	plt.plot(top_x, top_y)
	plt.xlabel('Размерность чисел, 10^x')
	plt.ylabel('Время, мс')
	plt.title('Измерение времени работы при фиксированном количестве объектов')
	plt.show()

	plt.plot(length_x, length_y)
	plt.xlabel('Количество элементов, единиц')
	plt.ylabel('Время, мс')
	plt.title('Измерение времени работы при фиксированной размерности объектов')
	plt.show()


if __name__ == '__main__':
	raw, res, time_delta = measure(10, 1000)
	print('Raw: {}\nResult: {}\nTime: {}ms'.format(raw, res, time_delta * 1000))

	graph()