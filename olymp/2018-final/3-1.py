n = int(input())

def s(n, i):
	k = 0
	while not n%i:
		k += 1
		n = n // i
	return n, k

i = 2
f = False
while True:
	if not n%i:
		n, o = s(n, i)

		if f:
			print('*', end='')
		else:
			f = True
		print('%d^%d' % (i, o), end='')

		if n == 1:
			break

	i += 1