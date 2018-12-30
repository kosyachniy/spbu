import numpy as np 
import matplotlib.pyplot as plt 

def draw(T,X): 
	plt.scatter(T, X) 
	plt.show()

def f(t, x, g=9.8, l=1): 
	theta, ang_vel = x[0], x[1] 
	return np.array([ang_vel, -g*np.sin(theta)/l]) 


def step(F,T,X1,dt): 
	k1 = F(T,X1) 
	k2 = F(T + dt/2, X1 + k1*dt/2) 
	k3 = F(T + dt/2, X1 + k2*dt/2) 
	k4 = F(T + dt, X1 + k3*dt) 
	X2 = X1 + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6 
	return X2 

def rk4(F, t0, x0, t, dt=0.1): 
	n = int((t - t0) / dt) 

	if (t - t0 - n * dt) == 0: 
		n+=1 
	else: 
		n+=2 

	X = np.empty((n,2)) 
	X[0] = [x0,0] 
	T = np.empty(n) 
	T[0] = t0 

	for i in range(1,X.shape[0]-1): 
		X[i] = step(F,T[i-1],X[i-1],dt) 
		T[i] = T[i-1] + dt 

	dt = t - T[n-2] 
	X[n-1] = step(F,T[n-2],X[n-2],dt) 
	T[n-1] = T[n-2] + dt 
	draw(T, X[:,0]) 

	return X 


x1 = rk4(f, 0, np.pi/4, 100, dt=10) 
#x2 = rk4(f, 0, np.pi/4, 100, dt=1) 
#x3 = rk4(f, 0, np.pi/4, 100, dt=10) 
# plot numerical and precise solutions... 
print(x1)