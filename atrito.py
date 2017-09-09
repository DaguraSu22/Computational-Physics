from numpy import empty
from matplotlib.pyplot import plot, savefig, grid, legend, show, xlabel, ylabel
from gaussxw import gaussxw

def force1(k, x):
	return k**3*x**(4*k-3)
def force2(k, x):
	return k**3*x**(4*k-3)/(1 + k**2*x**(2*k-2))

def sympsons(N, a, b, f, n):
	h = (b-a)/N
	sum = f(n,a) + f(n, b)
	for k in range (1, N, 2):
		sum += 4*f(n,a + k*h)
	for k in range (2, N, 2):
		sum += 2*f(n,a + k*h)
	return (h/3)*sum

def gauss(N, a, b, f, n):
	# Calculate the sample points and weights, then map them
	# to the required integration domain
	x,w = gaussxw(N)
	xp = 0.5*(b-a)*x + 0.5*(b+a)
	wp = 0.5*(b-a)*w

	# Perform the integration
	s = 0.0
	for k in range(N):
   		s += wp[k]*f(n,xp[k])
	return s

N = 1000

F = empty (N, float)
X = empty (N, float)
l = 1/N
for j in range (1, N):
	F[j] = sympsons (N, 0.01 , 1, force2, l)
	X[j] = l
	l = l + 0.001
min = 2
k = 0
for j in range (1, N):
	if j>400 and F[j]<min:
		min = F[j]
		k = j 
print min, k
#plot (X, F)
#xlabel('n')
#ylabel('Force')
#savefig("atrito.png")
#show ()
