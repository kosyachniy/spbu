a = 'abcdefgh'
x = input()
x = (a.index(x[0]), int(x[1])-1)
y = input()
y = (a.index(y[0]), int(y[1])-1)

m = [[1 for i in range(8)] for j in range(8)]
n = []

def step(t0, t1, s='', k=1):
	print('!!!', k, t0, t1)
	m[t0][t1] = 0
	s += a[t0] + str(t1+1) + '\n'
	if t0 == y[0] and t1 == y[1]:
		n.append((len(s), s))
	else:
		for l in ((-2,1), (-1,2), (1,2), (2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)):
			tt0 = t0+l[0]
			tt1 = t1+l[1]
			if 0 <= tt0 <= 7 and 0 <= tt1 <= 7 and m[tt0][tt1]:
				step(tt0, tt1, s, k+1)

step(x[0], x[1])
print(sorted(n)[0][1], end='')