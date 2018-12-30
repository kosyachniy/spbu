n = int(input())
*o, r = map(int, input().split())
x = list(map(int, input().split()))
a, b = x[:n], x[n:]

import math

def circleSegmentIntersections(x1, y1, x2, y2, xc, yc, r):
    dx = x1 - x2
    dy = y1 - y2
    rx = xc - x1
    ry = yc - y1
    a = dx*dx + dy*dy
    b = dx*rx + dy*ry
    c = rx*rx + ry*ry - r*r
    # Now solve a*t^2 + 2*b*t + c = 0
    d = b*b - a*c
    if d < 0.:
        # no real intersection
        return None
    s = math.sqrt(d)
    t1 = (- b - s)/a
    t2 = (- b + s)/a
    if t1 >= 0. and t1 <= 1.:
        return ((1 - t1)*x1 + t*x2, (1 - t1)*y1 + t*y2)
    if t2 >= 0. and t2 <= 1.:
        return ((1 - t2)*x1 + t*x2, (1 - t2)*y1 + t*y2)

print(circleSegmentIntersections(a[0], b[0], a[1], b[1], o[0], o[1], r))