from one import dichotomy
import numpy as np
from scipy.optimize import line_search
from random import *

class vector(object):
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "({0}, {1})".format(*[round(i, 3) for i in self.x])

    def __add__(self, other):
        return vector([self.x[i] + other.x[i] for i in range(len(self.x))])

    def __sub__(self, other):
        return vector([self.x[i] - other.x[i] for i in range(len(self.x))])

    def __rmul__(self, other):
        return vector([self.x[i] * other for i in range(len(self.x))])

    def __truediv__(self, other):
        return vector([self.x[i] / other for i in range(len(self.x))])

    ret = lambda self: tuple(self.x)

def rast(x, y=0):
    x = x.ret()
    y = y.ret() if y else vector([0, 0]).ret()
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

def deformable_polyhedron(f, alpha=1, beta=0.5, gamma=2, delta=0.01):
    v1, v2, v3 = map(vector, [[0, 0], [1, 0], [0, 1]])

    while True: #for i in range(maxiter):
        dots = {v1: f(v1.ret()), v2: f(v2.ret()), v3: f(v3.ret())}
        b, g, w = [i[0] for i in sorted(dots.items(), key=lambda x: x[1])]

        mid = (g + b) / 2

        #Отражение
        xr = mid + alpha * (mid - w)
        if f(xr.ret()) < f(g.ret()):
            w = xr
        else:
            if f(xr.ret()) < f(w.ret()):
                w = xr
            c = (w + mid) / 2
            if f(c.ret()) < f(w.ret()):
                w = c

        if f(xr.ret()) < f(b.ret()):
            #Растяжение
            xe = mid + gamma * (xr - mid)
            w = xe if f(xe.ret()) < f(xr.ret()) else xr

        if f(xr.ret()) > f(g.ret()):
            #Сжатие
            xc = mid + beta * (w - mid)
            if f(xc.ret()) < f(w.ret()):
                w = xc

        if rast(v1, w) < delta and rast(v2, g) < delta and rast(v3, b) < delta:
            return b

        #Новые точки
        v1 = w
        v2 = g
        v3 = b

def gradient_descent(f, f1, f2, delta=0.001):
    x0 = vector([1., 1.])

    while True:
        p0 = vector([-f1(x0.ret()), -f2(x0.ret())])

        def x1(alpha):
            x = x0 + alpha * p0
            return f(x.ret())

        alpha = dichotomy(x1, 0, 5, delta, delta * 1.5)[0]

        xk = x0 + alpha * p0

        if rast(p0) < delta:
            return xk

        x0 = xk

def conjugate_gradients(f, f1, f2, delta=0.001):
    x = vector([1.1, 1.1])
    pk = vector([-f1(x.ret()), -f2(x.ret())])
    k=0

    while True:
        if not f(x.ret()): return x.ret()
        k += 1

        p = vector([-f1(x.ret()), -f2(x.ret())])

        def x1(alpha):
            xx = x + alpha * p
            return f(xx.ret())

        alpha = dichotomy(x1, 0, 5, delta, delta * 1.5)[0] #line_search(f, re, np.array(x.ret(), float), np.array(p.ret(), float))[0]

        xk = x + alpha * p

        if k % 2:
            x3 = vector([f1(xk.ret()), f2(xk.ret())])
            w = rast(x3) ** 2 / rast(vector([f1(x.ret()), f2(x.ret())])) ** 2
            d = w * pk
        else:
            d = vector([0, 0])

        pk = vector([-f1(xk.ret()), -f2(xk.ret())]) + d

        if rast(pk) < delta:
            return xk

        x = xk

def quasi_newtonian(f, f1, x=np.array([1, 1]), delta=0.001):
    gfk = f1(x)
    Hk = E = np.eye(len(x))
    l = 0
   
    while rast(vector(gfk)) > delta:
        l += 1
        pk = -np.dot(Hk, gfk)

        alpha = line_search(f, f1, x, pk)[0]
        
        xkp1 = x + alpha * pk

        '''
        def x1(alpha):
            xx = x + alpha * pk
            print(xx)
            return f(xx)
        alpha = dichotomy(x1, 0, 5, delta, delta * 1.5)
        xkp1 = x + alpha * pk
        '''

        sk = xkp1 - x
        gfkp1 = f1(xkp1)
        yk = gfkp1 - gfk

        if l % 2:
            ro = 1. / np.dot(yk, sk)
            A1 = E - ro * sk[:, np.newaxis] * yk[np.newaxis, :]
            A2 = E - ro * yk[:, np.newaxis] * sk[np.newaxis, :]
            Hk = np.dot(A1, np.dot(Hk, A2)) + (ro * sk[:, np.newaxis] * sk[np.newaxis, :])
        else:
            Hk = E
        #print(Hk)

        '''
        re = sk - np.dot(Hk, yk)
        Hk = Hk + (re * re.T) / (re.T * yk)
        #print(Hk)
        '''

        x = xkp1
        gfk = gfkp1
        
    return tuple(round(i, 2) for i in x)


if __name__ == '__main__':
    f1 = lambda x: 100 * (x[1] - x[0] ** 2) ** 2 + 5 * (1 - x[0]) ** 2
    f2 = lambda x: (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2

    f1p1 = lambda x: np.array([-400 * x[0] * (x[1] - x[0] ** 2) - 10 * (1 - x[0]), 200 * (x[1] - x[0] ** 2) ** 2])
    f2p1 = lambda x: np.array([4 * x[0] * (x[0] ** 2 + x[1] - 11) + 2 * (x[0] + x[1] ** 2 - 7), 2 * (x[0] ** 2 + x[1] - 11) + 4 * x[1] * (x[0] + x[1] ** 2 - 7)])

    f1x1 = lambda x: -400 * x[0] * (x[1] - x[0] ** 2) - 10 * (1 - x[0])
    f1x2 = lambda x: 200 * (x[1] - x[0] ** 2) ** 2
    f2x1 = lambda x: 4 * x[0] * (x[0] ** 2 + x[1] - 11) + 2 * (x[0] + x[1] ** 2 - 7)
    f2x2 = lambda x: 2 * (x[0] ** 2 + x[1] - 11) + 4 * x[1] * (x[0] + x[1] ** 2 - 7)

    print('Метод деформируемого многогранника')
    print(deformable_polyhedron(f1))
    print(deformable_polyhedron(f2))
    print('Метод градиентного спуска')
    print(gradient_descent(f1, f1x1, f1x2))
    print(gradient_descent(f2, f2x1, f2x2))
    print('Метод сопряжённых градиентов')
    print(conjugate_gradients(f1, f1x1, f1x2))
    print(conjugate_gradients(f2, f2x1, f2x2))
    print('Квазиньютоновкий метод')
    print(quasi_newtonian(f1, f1p1))
    print(quasi_newtonian(f2, f2p1))