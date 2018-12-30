from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show
def answer():
    print('Part a:')
    print(low(x,t))
    print('First Graph')
    print('')



def f(x, t, g=9.8, l=1):
  theta, ang_vel  = x[0], x[1]
  return np.array([ang_vel, -g*np.sin(theta)/l])


def low(x,t):
    return 1/RC * (V_in - V_out)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N
RC = 0.01
V_out = 0.0

tpoints = arange(a,b,h)
xpoints = []
x = 0.0

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

plot(tpoints,xpoints)
xlabel("t")
ylabel("x(t)")
show()