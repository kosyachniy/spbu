n = int(input())
m = [list(map(int, input().split())) for i in range(n)]

q = lambda x, y: ((3, 2), (4, 1))[x>0][y>0]

k = 0
s = 0
p_tg, p_q = m[0][1] / m[0][0], q(m[0])
for i, a in enumerate(m[1:]):
	t_tg = a[1] / a[0]
	t_q = q(a)

	if t_tg > p_tg or t_q > p_q or (t_q == 0)