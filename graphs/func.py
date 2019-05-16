import networkx as nx


# G = nx.DiGraph()
# G.add_nodes_from(['1', '2', '3', '4', '5'])
# G.add_edge('1', '2')
# G.add_edge('2', '4')
# G.add_edge('4', '5')
# G.add_edge('5', '2')
# G.add_edge('1', '3')
# G.add_edge('3', '5')

G = nx.read_gexf('vk-friends-140420515.gexf')


conn_weak = {i: [list(set(j)-{i})[0] for j in G.edges() if i in j] for i in G}
conn_strong = {i: list(G.neighbors(i)) for i in G}

# print(conn_weak)
# print(conn_strong)


# Максимальная компонента

nodes_tout = {i: -1 for i in G.nodes()}

def dfs(node, conn):
    nodes_tout[node] = 0
    component = [node]

    for contig in conn[node]:
        if nodes_tout[contig] == -1:
            component.extend(dfs(contig, conn))

    return component

component_max = []

for i in G.nodes():
    if nodes_tout[i] == -1:
        component = dfs(i, conn_weak)

        if len(component_max) < len(component):
            component_max = component + []

# Создаём мультиграф

H = nx.MultiGraph()

# H.add_nodes_from(G.nodes())
H.add_nodes_from(component_max)
for i in conn_strong:
	for j in conn_strong[i]:
		if j in component_max:
			H.add_edge(i, j)

conn = {i: [list(set(j)-{i})[0] for j in G.edges() if i in j] for i in G}