from one import dichotomy
import numpy as np
import numpy.linalg as ln
from scipy.optimize import line_search

class vector(object):
    def __init__(self, x):
        self.x1 = x[0]
        self.x2 = x[1]

    def __repr__(self):
        return "({0}, {1})".format(round(self.x1, 3), round(self.x2, 3))

    def __add__(self, other):
        x1 = self.x1 + other.x1
        x2 = self.x2 + other.x2
        return vector([x1, x2])

    def __sub__(self, other):
        x1 = self.x1 - other.x1
        x2 = self.x2 - other.x2
        return vector([x1, x2])

    def __rmul__(self, other):
        x1 = self.x1 * other
        x2 = self.x2 * other
        return vector([x1, x2])

    def __truediv__(self, other):
        x1 = self.x1 / other
        x2 = self.x2 / other
        return vector([x1, x2])

    def ret(self):
        return (self.x1, self.x2)

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
    x0 = vector([1, 1])

    while True:
        p0 = vector([-f1(x0.ret()), -f2(x0.ret())])

        def x1(alpha):
            x = x0 + alpha * p0
            return f(x.ret())

        alpha = dichotomy(x1, 0, 5, delta, delta * 1.5)[0]

        xk = x0 + alpha * p0

        if rast(xk, x0) < delta:
            return xk

        x0 = xk

def conjugate_gradients(f, f1, f2, delta=0.001):
    x = vector([1, 1])

    while True:
        if not f(x.ret()): return x.ret()

        p = vector([-f1(x.ret()), -f2(x.ret())])

        def x1(alpha):
            xx = x + alpha * p
            return f(x.ret())

        alpha = dichotomy(x1, 0, 5, delta, delta * 1.5)[0]

        xk = x + alpha * p

        x3 = vector([f1(xk.ret()), f2(xk.ret())])
        w = rast(x3) ** 2 / rast(-1 * x) ** 2

        p = vector([-f1(xk.ret()), -f2(xk.ret())]) + w * p

        if rast(p) < delta:
            return xk

        x = xk

def quasi_newtonian(f, f1, x0=np.array([1, 1]), maxiter=0, epsi=0.001):
    if not maxiter: maxiter = len(x0) * 200

    k = 0
    gfk = f1(x0)
    N = len(x0)
    I = np.eye(N, dtype=int)
    Hk = I
    xk = x0
   
    while ln.norm(gfk) > epsi and k < maxiter:
        pk = -np.dot(Hk, gfk)

        alpha = line_search(f, f1, xk, pk)[0]
        
        xkp1 = xk + alpha * pk
        sk = xkp1 - xk
        xk = xkp1
        
        gfkp1 = f1(xkp1)
        yk = gfkp1 - gfk
        gfk = gfkp1
        
        k += 1
        
        ro = 1.0 / (np.dot(yk, sk))
        A1 = I - ro * sk[:, np.newaxis] * yk[np.newaxis, :]
        A2 = I - ro * yk[:, np.newaxis] * sk[np.newaxis, :]
        Hk = np.dot(A1, np.dot(Hk, A2)) + (ro * sk[:, np.newaxis] * sk[np.newaxis, :])
        
    return tuple(round(i, 2) for i in xk)


if __name__ == '__main__':
    f1 = lambda x: 100 * (x[1] - x[0] ** 2) ** 2 + 5 * (1 - x[0]) ** 2
    f2 = lambda x: (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2

    f1p1 = lambda x: np.array([-400 * x[0] * (x[1] - x[0] ** 2) - 10 * (1 - x[0]), 200 * (x[1] - x[0] ** 2) ** 2])
    f2p2 = lambda x: np.array([4 * x[0] * (x[0] ** 2 + x[1] - 11) + 2 * (x[0] + x[1] ** 2 - 7), 2 * (x[0] ** 2 + x[1] - 11) + 4 * x[1] * (x[0] + x[1] ** 2 - 7)])

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
    print(quasi_newtonian(f2, f2p2))