a = 'abcdefgh'
x = input()
x = (a[x[0]], int(x[1]))
y = input()
y = (a[y[0]], int(y[1]))

m = [[0 for i in range(8)] for j in range(8)]
m[x[0]][x[1]] = 1
m[x[0]][x[1]] = -1

k = 0

for i in range(8):
	for j in range(8):
		if m[i][j] > k:
			for l in ((-2,1), (-1,2), (1,2), (2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)):
				try:
					if m[i+l[0]][j+l[1]] == -1:
						break
					else:
						m[i+l[0]][j+l[1]] += 1
				except:
					pass
		k += 1