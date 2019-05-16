import time

import networkx as nx
import matplotlib.pyplot as plt

from func import H as G, conn


check_connect = lambda i, j: j in conn[i]

# Гистограмма плотности вероятности распределения степеней вершин

vertex_count = []

for i in G.edges():
	vertex_count.extend(i)

node_count = {i: vertex_count.count(i) for i in G.nodes()}

# print(max(node_count.values()))
rasp = [0 for i in range(max(node_count.values())+1)]
for i in G.nodes():
	# print(node_count[i])
	rasp[node_count[i]] += 1

rasp = [i/len(G.nodes()) for i in rasp]

# print(rasp)

# Строим гистограмму

x = range(len(rasp))

ax = plt.gca()
ax.bar(x, rasp)

plt.show()

# Средняя степень вершины

node_count_sum = 0
for i in node_count:
	node_count_sum += node_count[i]

print('-' * 100)
print('Средняя степень вершины:', node_count_sum/len(G.nodes()))

# Находим длину пути до каждой точки

verhO = dict()
for i in G.nodes():
	verhU = {j: 0 for j in G.nodes()}
	verhU[i] = -1
	for j in G.nodes():
		if i != j and check_connect(i, j):
			verhU[j] = 1
	
	while 0 in verhU.values():
		# print('!!!', i, verhU)
		for j in G.nodes():
			if verhU[j] == 0:
				try:
					verhU[j] = (min([verhU[p] for p in G.nodes() if p != j and verhU[p] > 0 and check_connect(p,j)])+1) * (-1)
				except:
					pass
		
		for j in G.nodes():
			if j != i and verhU[j] < 0:
				verhU[j] *= -1
	
	verhU[i] = 0

	# print('---'*100)
	# print(i,'\n',time.time(),'\n',verhU)
	
	verhO[i] = verhU

# print(verhO)

# Записываем в файл

import csv

nodes = list(G.nodes())
matr = [['-'] + nodes] + [[i] + [0 for j in nodes] for i in nodes]

for ni, i in enumerate(nodes):
	for nj, j in enumerate(nodes):
		matr[ni+1][nj+1] = verhO[i][j]

with open('distance.csv', 'w') as file:
	for i in matr:
		csv.writer(file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(i)

# Радиус и диаметр

dl = 0
count = 0

for i in verhO:
	dl += sum(verhO[i].values())
	count += len(verhO) - 1
	verhO[i] = max(verhO[i].values())

r, d = min(verhO.values()), max(verhO.values())

print('-' * 100)
print('Радиус:', r)
print('Диаметр:', d)

# Центральные и периферийные вершины

print('-' * 100)
print('Центральные вершины:')
for i in verhO:
	if verhO[i] == r:
		print(i)

print('Перифирийные вершины:')
for i in verhO:
	if verhO[i] == d:
		print(i)

# Средняя длина пути в графе

print('-' * 100)
print('Средняя длина пути в графе:', dl/count)