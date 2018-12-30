n, m = map(int, input().split())
x = (input().split() for i in range(n))
x = {i[0]: True if i[1] == '1' else False for i in x}
y = (input().split() for i in range(m))

for i in y:
	try:
		j = 3
		while j < len(i):
			if i[j] == '&':
				i[j-1] = i[j-1] if type(i[j-1])==bool else x[i[j-1]] & i[j+1] if type(i[j+1])==bool else x[i[j+1]]
				del i[j]
				del i[j]
			else:
				j += 2

			print(i)

		j = 3
		while j < len(i):
			if i[j] == '|':
				i[j-1] = i[j-1] if type(i[j-1])==bool else x[i[j-1]] | i[j+1] if type(i[j+1])==bool else x[i[j+1]]
				del i[j]
				del i[j]

	except:
		print('?')
		x[i[0]] = '?'

	else:
		x[i[0]] = i[2]
		print(1 if i[2] else 0)