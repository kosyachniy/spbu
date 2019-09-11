import csv

import networkx as nx
import matplotlib.pyplot as plt

from func import H as G, conn


with open('distance.csv', 'r') as file:
	f = False
	for i in csv.reader(file, delimiter=',', quotechar=' '):
		if f:
			for j, el in enumerate(i[1:]):
				distance[i[0]][nodes[j]] = int(el)

		else:
			nodes = i[1:]
			distance = {j: dict() for j in nodes}
			f = True


# nodes = list(G.nodes())
conn = {i: set(conn[i]) for i in conn} 

# Метрика по степени

centrality_degree = dict()

for node in nodes:
    centrality_degree[node] = len(conn[node]) / (len(nodes) - 1)

print('-' * 100)
print('Метрика по степени:', centrality_degree)

x = [centrality_degree[i] for i in nodes]
nx.draw(G, pos=None, node_size=100, node_color=x)
plt.show()

# Метрика по близости

centrality_closeness = dict()

for node in nodes:
    centrality_closeness[node] = (len(nodes) - 1) / sum(distance[node].values())

print('-' * 100)
print('Метрика по близости:', centrality_closeness)

x = [centrality_closeness[i] for i in nodes]
nx.draw(G, pos=None, node_size=100, node_color=x)
plt.show()

# Метрика посредничества

from collections import defaultdict, deque

count_shortpath = defaultdict(lambda: 0)

for i in nodes:
    for j in nodes:
        node_parents = defaultdict(list)
        node_distance = {i : 0}
        q = deque()
        q.append(i)

        while q:
            node_current = q.popleft()

            for v in conn[node_current]:
                if not v in node_distance:
                    node_distance[v] = node_distance[node_current] + 1
                    q.append(v)

                if node_distance[v] == node_distance[node_current] + 1:
                    node_parents[v].append(node_current)
        
        membership_current = defaultdict(lambda: 0)
        membership_current[j] = 1
        q.append(j)

        while q:
            node_current = q.popleft()

            for v in node_parents[node_current]:
                if not v in membership_current:
                    q.append(v)

                membership_current[v] += membership_current[node_current]

        for t in membership_current:
            if t != i and t != j:
                count_shortpath[t] += membership_current[t] / membership_current[i]

# Нормализация

normalized_count_shortpath = {}
centrality_betweeness = dict()

for i in nodes:
    if not i in count_shortpath:
        normalized_count_shortpath[i] = 0
        centrality_betweeness[i] = normalized_count_shortpath[i]
        
for i in count_shortpath:
    normalized_count_shortpath[i] = count_shortpath[i] / (((len(nodes) - 1) * (len(nodes) - 2)) / 2) 
    centrality_betweeness[i] = normalized_count_shortpath[i]

print('-' * 100)
print('Метрика посредничества:', centrality_betweeness)

x = [centrality_betweeness[i] for i in nodes]
nx.draw(G, pos=None, node_size=100, node_color=x)
plt.show()

# Метрика центральности

from collections import defaultdict

from numpy import linalg as LA
import numpy as np

node_matrix = defaultdict(dict)

for i in nodes:
    for j in nodes:
        node_matrix[i][j] = 1 if j in conn[i] else 0

cur_id = 0
node_index = {}
from_index_to_node = {}
for node in nodes:
    node_index[node] = cur_id
    from_index_to_node[cur_id] = node
    cur_id += 1

    
real_g_matrix = [[0] * len(nodes) for i in range(len(nodes))]
for node in nodes:
    for v in conn[node]:
        real_g_matrix[node_index[node]][node_index[v]] = 1

        
def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)

def power_iteration(A):
    n, d = A.shape

    v = np.ones(d) / np.sqrt(d)
    ev = eigenvalue(A, v)

    while True:
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)

        ev_new = eigenvalue(A, v_new)
        if np.abs(ev - ev_new) < 0.01:
            break

        v = v_new
        ev = ev_new

    return ev_new, v_new

        
np_shrinked_matrix = np.array(real_g_matrix)

eigen_values, eigen_vector = power_iteration(np_shrinked_matrix)

# print(eigen_values, eigen_vector)

centrality_eigen_vector = dict()

for i in range(len(eigen_vector)):
    centrality_eigen_vector[from_index_to_node[i]] = eigen_vector[i]
    
print('-' * 100)
print('Метрика центральности:', centrality_eigen_vector)

x = [centrality_eigen_vector[i] for i in nodes]
nx.draw(G, pos=None, node_size=100, node_color=x)
plt.show()

# Метрика Edge betweeness

from collections import defaultdict

from collections import deque

shortest_path_edge_membership_count = defaultdict(lambda: 0)

for i in nodes:
    for j in nodes:
        
        node_parents = defaultdict(list)
        node_distance = {i : 0}
        q = deque()
        q.append(i)
        while q:
            node_current = q.popleft()
            for v in conn[node_current]:
                if not v in node_distance:
                    node_distance[v] = node_distance[node_current] + 1
                    q.append(v)
                if node_distance[v] == node_distance[node_current] + 1:
                    node_parents[v].append(node_current)
                    
        membership_current = defaultdict(lambda: 0)
        membership_current[j] = 1
        cur_edge_membership = defaultdict(lambda: 0)
        q.append(j)
        while q:
            node_current = q.popleft()
            for v in node_parents[node_current]:
                if not v in membership_current:
                    q.append(v)
                cur_edge_membership[(min(node_current, v), max(node_current, v))] += membership_current[node_current]
                membership_current[v] += membership_current[node_current]
        for t in cur_edge_membership:
            shortest_path_edge_membership_count[t] += cur_edge_membership[t] / membership_current[i]

centrality_betweenes = defaultdict(dict)
normalized_shortest_path_edge_membership_count = shortest_path_edge_membership_count

for i in normalized_shortest_path_edge_membership_count:
    normalized_shortest_path_edge_membership_count[i] = normalized_shortest_path_edge_membership_count[i] / (((len(nodes)) * (len(nodes) - 1)) / 2) 
    centrality_betweenes[i] = normalized_shortest_path_edge_membership_count[i]

print('-' * 100)
print('Метрика Edge betweeness:', centrality_betweenes)

# Если вдруг что, смотри предыдущую версию файла !!!

x = [centrality_betweenes[i, j] for i, j in G.edges()]
print(*[(i, j, centrality_betweenes[i, j]) for i, j in G.edges()], sep='\n')
x = [i if type(i) != dict else 0 for i in x]
# print(max(x))

nx.draw(G, pos=None, node_size=100, edge_color=x)
plt.show()