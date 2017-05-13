import numpy as np
import matplotlib.pyplot as plt

# Declaracao das constantes
G = 6.674e-11 # Constante de gravitacao universal
M = 5.974e24 # Massa do Sol
m = 7.348e22 # Massa da Lua
R = 3.844e8 # Distancia entre o centro da lua e o centro da Terra
w = 2.662e-6 # Velocidade angular da rotacao da Lua em torno do Sol

r = np.linspace(-1e9, 1e9, 100000)
plt.plot(r, w*w*r**5 - 2*w*w*R*r**4 + w*w*R*R*r**3 + G*m*r*r - G*M*r*r + 2*G*M*R*r - G*M*R*R)
plt.xlabel('r')
plt.ylabel('p(r)')
plt.grid()
plt.savefig('ex5a.png')
plt.show ()

