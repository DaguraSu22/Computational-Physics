from __future__ import division, print_function
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import time
start_time = time.time()
# Constants
M = 9        	# Grid squares on a side
V = 1.0         # Voltage at top wall
target = 1e-6   # Target accuracy

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float)
phiprime = empty([M+1,M+1],float)
#phi[0,:] = V

# Main loop
cont = 0
delta = 1.0
omega = 0.0

while delta>target:
	delta = 0
	# Calcula os valores do novo potencial
	for i in range(1,M):
		for j in range(1,M):
			if i>(0.7*M/2) and i<(1.3*M/2) and j>(0.7*M/2) and j<(1.3*M/2):
				phi[i,j] = 1
		    	else:
				difference = (phi[i+1,j] + phi[i-1,j] \
				                 + phi[i,j+1] + phi[i,j-1])/4 - phi[i,j]
			    	phi[i,j] = phi[i,j] + (1+omega)*difference
			if difference>delta: delta = difference
	phi,phiprime = phiprime,phi
	cont =  cont + 1
print("--- %s seconds ---" % (time.time() - start_time))
print(cont)


# Surface plot

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(0, M+1, 1)
Y = np.arange(0, M+1, 1)
X, Y = np.meshgrid(X, Y)
Z = phi[:]

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                      linewidth=0, antialiased=False)

plt.show()

# Make a plot
imshow(phi.T,origin='lower')
#gray()
colorbar()
show()
