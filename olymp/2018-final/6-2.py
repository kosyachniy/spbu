n, m = map(int, input().split())
x = (input().split() for i in range(n))
x = {i[0]: True if i[1] == '1' else False for i in x}

for o in range(m):
	i = input().split()

	try:
		for j in range(2, len(i), 2):
			i[j] = x[i[j]]
	except:
		print('?')
		x[i[0]] = '?'

	else:
		if '?' in i:
			print('?')
			x[i[0]] = '?'

		else:
			j = 3
			while j < len(i):
				if i[j] == '&':
					i[j-1] = i[j-1] & i[j+1]
					del i[j]
					del i[j]
				else:
					j += 2

			j = 3
			while j < len(i):
				if i[j] == '|':
					i[j-1] = i[j-1] | i[j+1]
					del i[j]
					del i[j]

			x[i[0]] = i[2]
			print(1 if i[2] else 0)