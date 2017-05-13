import numpy as np

# Declaracao das constantes
G = 6.674e-11 # Constante de gravitacao universal
M = 5.974e24 # Massa do Sol
m = 7.348e22 # Massa da Lua
R = 3.844e8 # Distancia entre o centro da lua e o centro da Terra
w = 2.662e-6 # Velocidade angular da rotacao da Lua em torno do Sol

r = np.linspace(-4e9, 4e9, 10**6)
y =  5*w*w*r**4 - 8*w*w*R*r**3 + 3*w*w*R*R*r**2 + 2*G*m*r - 2*G*M*r + 2*G*M*R
for n in y:
	if(n<0):
		print "A derivada eh negativa"


