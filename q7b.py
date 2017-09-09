from numpy.linalg import eigvalsh, eigh
from numpy import empty,sin,arange, linspace
from matplotlib.pyplot import plot, savefig, grid, legend
from math import pi, sqrt

#Constants
L = 5e-10
q = 1.6022e-19
a = 10*q
M = 9.1094e-31
hbar = 1.0546e-34

def H(m,n):
	s=0
	
	if m==n:
		s+= (hbar*pi*n)**2/(2*M*L**2) + a/2
	if (m+n)%2 == 1:
		s+= -(8*a*m*n)/(pi**2*(m**2-n**2)**2)
	else:
		s+=0
	
	return s
def Hp(m,n):
	s=0
	
	if m==n:
		s+= hbar**2/8/M*pi**2*n**2
	
	def I(m,n):
		
		if m==n:
			return L**2/4
		elif (m+n)%2 == 1:
			return -(2*L/pi)**2* m*n/(m**2-n**2)**2
		else:
			return 0
	
	s += a/2*I(m,n)
	return s
N = 10
A = empty((N,N),float)
for i in range(N):
	for j in range(N):
		A[i,j] = H(i+1,j+1)

X,ksi = eigh(A)
print(X[:10])

def wavefunction(x,m=1):
	n = arange(1,N+1)
	s = sum(sqrt(2/L)*ksi[:,m]*sin(pi*n*x/L))
	return s**2

x = linspace(0,L,100)

for i in range(3):
	ksi_i = [wavefunction(xi,m=i) for xi in x]
	plot(x,ksi_i,label=i)
legend()
savefig('fig7.png')
for i in range (3):
	print ((2/L)*trapezoidal (50 , 0, L, wavefunction ,i))
