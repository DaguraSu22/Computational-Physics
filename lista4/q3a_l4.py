import numpy as np
import matplotlib.pyplot as plt

# Declaracao das constantes
m = 9.1094e-31
w = 1.0000e-9
h = 6.582119514e-16
V = 20.1
E = np.linspace(0.1, 20, 100)

# Impressao dos graficos
plt.plot(E, np.tan(np.sqrt((w*w*m*E)/(2*h*h*1.6e-19))))
plt.plot(E, np.sqrt((V - E)/E))
plt.plot(E, -np.sqrt(E/(V - E)))
plt.xlabel('Energia (eV)')
plt.ylabel('y')
plt.legend(["y1", "y2", "y3"], loc="upper left")
plt.savefig('ex3a.png')
plt.show()
