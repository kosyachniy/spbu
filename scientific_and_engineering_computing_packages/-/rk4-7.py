import numpy as np
import matplotlib.pyplot as plt

def f(t, x, g=9.8, l=1):
	theta, ang_vel = x[0], x[1]
	return np.array([ang_vel, -g*np.sin(theta)/l])

def rk4(F, t0, x0, t, dt=0.1): 
	n = (t - t0) // dt
	n += 2 if (t - t0 - n * dt) else 1

	X = np.empty((n, 2))
	T = np.empty(n)
	X[0], T[0] = x0, t0 

	for i in range(1, X.shape[0] - 1):
		X[i] = rk4_step(F, T[i-1], X[i-1], dt)
		T[i] = T[i-1] + dt

	dt = t - T[n-2]
	X[n-1] = rk4_step(F, T[n-2], X[n-2], dt)
	T[n-1] = T[n-2] + dt

	return X, T

def rk4_step(F, T, X1, dt):
	k1 = F(T, X1)
	k2 = F(T + dt/2, X1 + k1*dt/2)
	k3 = F(T + dt/2, X1 + k2*dt/2)
	k4 = F(T + dt, X1 + k3*dt)
	return X1 + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6


x, t = rk4(f, 0, np.pi/4, 100, dt=10)

# plot numerical and precise solutions...
print(x)

plt.plot(t, x[:, 0]) 
plt.show()