import networkx as nx
import csv

from func import G


# Матрица смежности

nx.to_pandas_adjacency(G).to_csv('contig_matrix.csv')

# Список смежности

# conn = {i: [j[1] for j in G.edges() if j[0] == i] for i in G}
conn_weak = {i: [list(set(j)-{i})[0] for j in G.edges() if i in j] for i in G}

conn_strong = {i: list(G.neighbors(i)) for i in G}
contig_list = ((i, *conn_strong[i]) for i in conn_strong)

# print(conn_weak)
# print(conn_strong)

with open('contig_list.csv', 'w') as file:
	for i in contig_list:
		csv.writer(file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(i)

# Слабая связность

nodes_tout = {i: -1 for i in G.nodes()}
components_count = 0
tout = 0

def dfs(node, conn):
    nodes_tout[node] = 0
    component = [node]
    global tout

    for contig in conn[node]: # ((oriented and conn_strong) or (not oriented and conn_weak))[node]:
        if nodes_tout[contig] == -1:
            component.extend(dfs(contig, conn))

    tout += 1
    nodes_tout[node] = tout
    return component

print('-' * 100)
print('Компоненты слабой связности')

component_max = []

for i in G.nodes():
    if nodes_tout[i] == -1:
        components_count += 1
        component = dfs(i, conn_weak)

        if len(component_max) < len(component):
            component_max = component + []

        print('#{}: {} ({})'.format(components_count, len(component), ', '.join(component)))

print('-' * 100)
print('Количество компонент слабой связности:', components_count)

if components_count == 1:
    print('Слабосвязный')
else:
    print('Не слабосвязный')

print('-' * 100)
print('Доля узлов наибольшей компоненты слабой связности:', len(component_max) / len(G.nodes()))

# Сильная связность

print('-' * 100)
print('Компоненты сильной связности')

Gt = nx.reverse_view(G)
conn_strong_trans = {i: list(Gt.neighbors(i)) for i in Gt}
# conn_strong_trans = {i: conn_strong[i][::-1] for i in conn_strong}

nodes_tout = {i: -1 for i in G.nodes()}
components_count = 0
tout = 0

for i in G.nodes():
    if nodes_tout[i] == -1:
        components_count += 1
        component = dfs(i, conn_strong_trans)



# nodes_visited = {i: False for i in G.nodes()}
fu, nodes_tout = nodes_tout, {i: -1 for i in G.nodes()}

components_count = 0

fu = list(map(lambda x: x[1], sorted([(fu[i], i) for i in fu])[::-1]))

for i in fu:
    if nodes_tout[i] == -1:
        components_count += 1
        component = dfs(i, conn_strong)

        print('#{}: {} ({})'.format(components_count, len(component), ', '.join(component)))

print('-' * 100)
print('Количество компонент сильной связности:', components_count)

if components_count == 1:
    print('Сильносвязный')
else:
    print('Не сильносвязный')