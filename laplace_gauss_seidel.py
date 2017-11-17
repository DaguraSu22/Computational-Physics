from __future__ import division, print_function
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import time
start_time = time.time()
# Constantes
M = 5001        	# Numero de pontos da grade.
V = 1.0         	# Tensao no interior do condutor.
target = 1e-2   	# Precisao.
# Inicializacao de variaveis
phi = zeros([M+1,M+1],float)
phiprime = empty([M+1,M+1],float)
# Metodo
cont = 0
delta = 1.0
while delta>target:
	delta = 0
	for i in range(1,M):
		for j in range(1,M):
			if i>(0.7*M/2) and i<(1.3*M/2) and j>(0.7*M/2) and j<(1.3*M/2):
				phi[i,j] = 1
		    	else:
				difference = (phi[i+1,j] + phi[i-1,j] \
				                 + phi[i,j+1] + phi[i,j-1])/4 - phi[i,j]
			    	phi[i,j] = phi[i,j] + difference
			if difference>delta: delta = difference
	phi,phiprime = phiprime,phi
	cont =  cont + 1
print("--- %s seconds ---" % (time.time() - start_time))
print(cont)



