import numpy as np
import scipy.optimize

def P(x):
	return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1 
def dP(x):
	return 4620*x**5 - 13860*x**4 + 12600*x**3 - 5040*x**2 + 840*x - 42

x_0 = float(input())
print scipy.optimize.newton(P, x_0, dP, tol=1e-10, maxiter=1500)

