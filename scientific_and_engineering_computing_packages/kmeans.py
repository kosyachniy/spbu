import numpy as np
import math
from numpy import linalg as LA

def calc_eps(X, k=0.01):
    min_dist = np.linalg.norm(X[0] - X[1], 1)
    for i in range(0, X.shape[0]):
        for j in range(0, X.shape[0]):
            dist = min_dist = np.linalg.norm(X[i] - X[j], 1)
            if dist < min_dist:
                min_dist = dist
    return k * min_dist

def assign_clusters(X, clusters):
    cluster_labels = np.zeros(X.shape[0])
    for i in range(0, X.shape[0]):
        k = 0
        minx = LA.norm(X[i] - clusters[0], 1)
        for j in range(1, clusters.shape[0]):
            x = LA.norm(X[i] - clusters[j], 1)
            if (x < minx):
                minx = x
                k = j
        cluster_labels[i] = k
    return cluster_labels

def update_clusters(X, cluster_labels):
    m = max(cluster_labels) + 1
    new_clusters = np.zeros(((int(m), X.shape[1])))
    for i in range(int(m)):
        S = 0
        for j in range(cluster_labels.shape[0]):
            if (cluster_labels[j] == i):
                S += 1
                new_clusters[i] += X[j]
        new_clusters[i] /= S
    return new_clusters

def is_converged(clusters, updated_clusters, eps):
    if (np.max(abs((clusters - updated_clusters))) > eps):
        return False
    return True

def kmeans(X, k, eps=None):
    # print(X)
    if not eps: eps = calc_eps(X)

    clusters = X[np.random.choice(X.shape[0], k, replace=False), :]
    while True:
        labels = assign_clusters(X, clusters)
        print(labels)
        new_clusters = update_clusters(X, labels)
        
        if is_converged(clusters, new_clusters, eps): break
        
        clusters = new_clusters

    return clusters


import random
def init_board(N):
    # return np.array([random.randint(-10, 10) for i in range(N)])
    return np.array([[random.randint(-10, 10), random.randint(-10, 10)] for i in range(N)])
    # return np.array([[random.randint(0, 1) for i in range(N)] for j in range(N)])

print(kmeans(init_board(20), 4))

# X = np.array([[1,1],[1,2],[4,4],[5,5],[5,4],[5,6], [1,9],[2,9]])
# S = kmeans(X, 5)
# print(S)
