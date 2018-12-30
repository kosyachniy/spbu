n = int(input())
m = [list(map(int, input().split())) for i in range(n)]
m = [i[1]/i[0] if i[0] else 1000000001 for i in m]

a = [[1, [0]]]
for i, b in enumerate(m):
	if len(m)-i > max(i[0] for i in a) and b < m[a[-1][1][0]]:
		a.append([1, [i]])

	for j in range(len(a)):
		if b > m[a[j][1][-1]]:
			a[j][1].append(i)
			a[j][0] += 1

a = sorted(a)[-1]
print(a[0])
print(*[i+1 for i in a[1]], sep=' ')