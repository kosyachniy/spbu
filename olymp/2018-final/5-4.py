a = 'abcdefgh'
x = input()
x = (a.index(x[0]), int(x[1])-1)
y = input()
y = (a.index(y[0]), int(y[1])-1)

km = 0
n = []

def step(t0, t1, s=[], k=1):
	global km
	global n

	s.append([t0, t1])
	if t0 == y[0] and t1 == y[1]:
		if not km or km > k:
			km = k
			n = s
	else:
		for l in ((-2,1), (-1,2), (1,2), (2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)):
			tt0 = t0+l[0]
			tt1 = t1+l[1]
			if 0 <= tt0 <= 7 and 0 <= tt1 <= 7 and [tt0, tt1] not in s and (not km or k<km):
				step(tt0, tt1, s+[], k+1)

step(x[0], x[1])
for i in n:
	print(a[i[0]]+str(i[1]+1))