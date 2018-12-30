n = int(input())
m = [input().split() for i in range(n)]
m = [int(i[1])/int(i[0]) if i[0]!='0' else 1000000001 for i in m]
s = sum(m) / n
print(m, s)

i = 0
while True:
	if m[i] <= s:
		break
	i += 1

a = [i]
for j in range(i+1, len(m)):
	if m[j] > m[a[-1]]:
		a.append(j)

print(len(a))
print(*[i+1 for i in a], sep=' ')