import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt("saida4.txt", float)

x = dados[:,0]
y = dados[:,1]

plt.plot(y,x, 'ro')
plt.xlabel('Temperatura (C)')
plt.ylabel('Temperatura (F)')
plt.xlim(-60,125)
plt.ylim(-5,105)
plt.savefig('ex4.png')
plt.show()

