import numpy as np

a = [[2, 6, 7], [1, 0, 3], [7, 7, 3]]

'''
for i in range(len(a)):
	a[i] = a[i] + [0]
'''

a = np.array(a)
print(a)

'''
u = []
for i in a:
	ure = []
	for j in i:
		ure.append(j)
	u.append(ure)
'''

n = a.shape[1]
print(n)

u = [[a[0][j] for j in range(n)]]
l = [[a[j][0] / u[0][0]] for j in range(n)]

'''
l = []
for i in a.T:
	lre = []
	for j in i:
		lre.append(j / u[1][1])
'''

for i, el in enumerate(a[1:]):
	print(i, u, l)
	u.append([0] * (i+1) + [el[j] - sum([l[i+1][k] * u[k][j] for k in range(i)]) for j in range(i+1, n)])

	print(u, u[i+1][i+1])
	re1 = (1 / u[i+1][i+1])
	for j in range(i+1, n):
		l[j].append(re1 * (a[j][i+1] - sum([l[j][k] * u[k][i+1] for k in range(i)])))

print(u, l)