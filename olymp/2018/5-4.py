n = int(input())
m = [list(map(int, input().split())) for i in range(n)]

k = 1
s = 0
p_tg = m[0][1] / m[0][0]
for i, a in enumerate(m[1:]):
	t_tg = a[1] / a[0]

	if t_tg > p_tg:
		k += 1
	else:
		k = 1
		s = i + 1

	p_tg = t_tg

print(k)
print(*range(s+1, s+k+1))