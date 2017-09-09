import numpy as np
import matplotlib.pyplot as plt
from pylab import imshow, colorbar, show
from math import *
from scipy import arange

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def Bmn(m,n):
	return (1 + (-1)**(m+1)*(1 + (-1)**(n+1)))/(m**3*n**3)
def u(x, y, t, M, N):
	t1 = 576.0/pi**6
	u0 = 0.0
	for n in range(1, N):
		for m in range (1, M):
			Bmn = (1 + (-1)**(m+1))*(1 + (-1)**(n+1))/(m**3*n**3)
			u0 += Bmn*np.sin(0.5*m*pi*x)*np.sin(n*np.pi*y/3.0)*np.cos(pi*np.sqrt(9*m**2 + 4*n**2)*t)
	u0 = t1*u0
	return u0

dx = 2.0/500.0
dz = dx
i = 0
j = 0
uxt0 = np.zeros([50,76])
for x in arange(0.0,2.0,0.04):
	for y in arange(0.0,3.0,0.04):
		#print i, j
		uxt0[i][j] = np.float64(u(x,y,13,50,50))
		j = j + 1
		if j > 75:
			j = 0
		#print uxt0[x][y]
	i = i + 1
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0, 50, 1)
Y = np.arange(0, 50, 1)
Z = uxt0
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

imshow(uxt0)
show()
colorbar()