import numpy as np
import matplotlib.pyplot as plt

def f(t, x, g=9.8, l=1):
  theta, ang_vel  = x[0], x[1]
  return np.array([ang_vel, -g*np.sin(theta)/l])

def step(f,t0,x0,dt):
  k1 = f(t0, x0)
  k2 = f(t0+dt/2, x0+dt*k1/2)
  k3 = f(t0+dt/2, x0+dt*k2/2)
  k4 = f(t0+dt, x0+dt*k3)

  return x0 + dt/6 * (k1 + 2*k2 + 2*k3 + k4)

def rk4(F, t0, x0, t, dt=0.1):
  val = np.append(np.arange(t0, t, dt), t)

  X = np.zeros((len(val), x0.shape[0]))
  X[0] = x0

  for i,t0 in enumerate(val[:-2]):
    dt = val[i+1] - t0
    x0 = step(F,t0,x0,dt)
    X[i] = x0
  
  return X, val


x1, t1 = rk4(f, 0, np.array([np.pi/4, 0]), 100, dt=0.1)
plt.plot(t1, x1[:,0])

plt.savefig('graph.png')
