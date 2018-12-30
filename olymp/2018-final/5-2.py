a = 'abcdefgh'
x = input()
x = (a.index(x[0]), int(x[1])-1)
y = input()
y = (a.index(y[0]), int(y[1])-1)

m = [[1 for i in range(8)] for j in range(8)]
km = 0
n = ''

def step(t0, t1, s='', k=1):
	global km
	global n

	print('!!!!!!!', k, t0, t1)
	s += a[t0] + str(t1+1) + '\n'
	print('!', t0, y[0], t1, y[1])
	if t0 == y[0] and t1 == y[1]:
		if not km or km > k:
			km = k
			n = s
	else:
		for l in ((-2,1), (-1,2), (1,2), (2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)):
			tt0 = t0+l[0]
			tt1 = t1+l[1]
			if k == 1: print('!'*100, '\n', tt0, tt1, 0 <= tt0 <= 7, 0 <= tt1 <= 7, m[tt0][tt1], (not km or k<km))
			if 0 <= tt0 <= 7 and 0 <= tt1 <= 7 and m[tt0][tt1] and (not km or k<km):
				step(tt0, tt1, s, k+1)

step(x[0], x[1])
print(n, end='')