from __future__ import division, print_function
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# Constants
M = 101        # Grid squares on a side
V = 1.0         # Voltage at top wall
target = 1e-6   # Target accuracy

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float)
#phi[0,:] = V
#phiprime = empty([M+1,M+1],float)

# Main loop
delta = 1.0
omega = 0.8
while delta>target:

    delta = 0
    # Calculate new values of the potential
    for i in range(1,M):
        for j in range(1,M):
            #if i==0 or i==M or j==0 or j==M:
             #   phiprime[i,j] = phi[i,j]
            
            if i>35 and i<65 and j>35 and j<65:
                phi[i,j] = 1
            #elif i==80 and j>20 and j<80:
	    # 		phi[i,j] = -1
            else:
	            difference = (phi[i+1,j] + phi[i-1,j] \
	                                 + phi[i,j+1] + phi[i,j-1])/4 - phi[i,j]
	            phi[i,j] = phi[i,j] + (1+omega)*difference
            if difference>delta: delta = difference
x = len(phi[:])
y = len(phi[1,:])

print (x,y)

# Surface plot

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(0, 102, 1)
Y = np.arange(0, 102, 1)
X, Y = np.meshgrid(X, Y)
Z = phi[:]

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

plt.show()

# Make a plot
#imshow(phi.T,origin='lower')
#gray()
#colorbar()
#show()
