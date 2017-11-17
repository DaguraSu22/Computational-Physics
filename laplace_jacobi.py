from numpy import empty,zeros,max
import numpy as np
import time
# Inicio da contagem de tempo.
start_time = time.time()
# Constantes.
M = 9         	# Numero de pontos da grade.
V = 1.0         # Tensao no interior do condutor.
target = 1e-6  	# Precisao.
# Inicializacao de variaveis.
phi = zeros([M+1,M+1],float)
phi[0,:] = 0
phiprime = empty([M+1,M+1],float)
cont = 0
# Procedimento.
delta = 1.0
while delta>target:
	for i in range(1,M):
		for j in range(1,M):
			if i>(0.7*M/2) and i<(1.3*M/2) and j>(0.7*M/2) \
			and j<(1.3*M/2):
				phiprime[i,j] = 1.0
			else:
				phiprime[i,j] = (phi[i+1,j] + phi[i-1,j] \
					+ phi[i,j+1] + phi[i,j-1])/4
	delta = max(abs(phi-phiprime))
	phi,phiprime = phiprime,phi
	cont =  cont + 1
print ("--- %s segundos ---" % (time.time() - start_time))
print (cont)



