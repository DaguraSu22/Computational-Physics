import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1000)
p_x = 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1
print np.diff(p_x)
# Impressao dos graficos
plt.plot(x, p_x)
plt.title('Sexto Polinomio de Legendre')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.savefig('ex4.png')
plt.show()

