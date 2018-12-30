from PIL import Image
import numpy as np
import math
from numpy import linalg as LA


def calc_eps(X, k=0.01):
    min_dist = np.linalg.norm(X[0]-X[1], 1)
    for i in range(0, X.shape[0]):
        for j in range(0, X.shape[0]):
            dist = min_dist = np.linalg.norm(X[i]-X[j], 1)
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
    if not eps: eps = calc_eps(X)

    clusters = X[np.random.choice(X.shape[0], k, replace=False), :]
    while True:
        labels = assign_clusters(X, clusters)
        print(labels)
        new_clusters = update_clusters(X, labels)
        
        if is_converged(clusters, new_clusters, eps): break
        
        clusters = new_clusters

    return clusters

def rgb2h(img):
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]

    h = np.zeros((img.shape[0], img.shape[1]))

    max_val = img.max(axis=2)
    min_val = img.min(axis=2)

    var0 = (max_val == min_val)
    h[var0] = 0

    var1 = (max_val != min_val) & (max_val == r) & (g < b)
    h[var1] = 60 * (g[var1] - b[var1]) / (max_val[var1] - min_val[var1]) + 360

    var2 = (max_val != min_val) & (max_val == r) & (g >= b)
    h[var2] = 60 * (g[var2] - b[var2]) / (max_val[var2] - min_val[var2]) + 0

    var3 = (max_val != min_val) & (max_val == g)
    h[var3] = 60 * (b[var3] - r[var3]) / (max_val[var3] - min_val[var3]) + 120
    
    var4 = (max_val != min_val) & (max_val == b)
    h[var4] = 60 * (r[var4] - g[var4]) / (max_val[var4] - min_val[var4]) + 240

    return h

def cluster_labels2img(labels, arr):
    arr[labels == 0] = [255, 0, 0]
    arr[labels == 1] = [0, 255, 0]
    arr[labels == 2] = [0, 0, 255]
    return arr


arr = np.array(Image.open('photo.png'))

m = arr.shape[0]
n = arr.shape[1]
h = rgb2h(arr)
h = np.reshape(h, (m * n, 1))

labels = kmeans(h, 3, 0.1)

arr = cluster_labels2img(labels, np.reshape(arr, (m * n, 3)))
arr = np.reshape(arr, (m, n, 3))

img = Image.fromarray(arr, 'RGB')
img.save('photo_clastered.jpg')
img.show()
