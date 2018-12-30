n = int(input())
m = [list(map(int, input().split())) for i in range(n)]
m = [i[1]/i[0] if i[0] else 1000000001 for i in m]
l_m = len(m)

a = [[1, [0]]]
max_l = 1
for i, b in enumerate(m):
	if len(m)-i > max(j[0] for j in a) and b < m[a[-1][1][0]]:
		a.append([1, [i]])

	for j in range(len(a)):
		if b > m[a[j][1][-1]]:
			a[j][1].append(i)
			a[j][0] += 1
			if a[j][0] > max_l:
				max_l = a[j][0]

a = sorted(a)[-1]
print(a[0])
print(*[i+1 for i in a[1]], sep=' ')