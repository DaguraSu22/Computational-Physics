from numpy import empty, linspace
from matplotlib.pyplot import plot, savefig, grid, legend, show

def y(k, x):
	return x**(k)


x = linspace (0.1,1,10000)


plot (x, y(0.7, x))
show ()