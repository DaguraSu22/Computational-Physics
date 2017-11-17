from math import sqrt,exp
from numpy import empty
from random import random,randrange, seed
#from visual import sphere,curve,display
from numpy import array, linspace,arange
from pylab import plot, show, legend, savefig,grid, ylim


N = 25
R = 0.02
Tmax = 10.0
Tmin = 1e-3
tau = 1e4

seed(1)
def f(q):
	return 1
	#if q<2:
	#	return 2-q
	#else:
	#	return 1
# Function to calculate the magnitude of a vector
def mag(x):
    return sqrt(x[0]**2+x[1]**2)

# Function to calculate the total length of the tour
def distance():
    s = 0.0
    for i in range(N):
        s += mag(r[i+1]-r[i])
    return s

# Choose N city locations and calculate the initial distance
r = empty([N+1,2],float)
for i in range(N):
    r[i,0] = random()
    r[i,1] = random()
r[N] = r[0]
D = distance()
'''
# Set up the graphics
display(center=[0.5,0.5])
for i in range(N):
    sphere(pos=r[i],radius=R)
l = curve(pos=r,radius=R/2)
'''
NN = 10
q =	0	
y = []
qp = []
for x in range(NN):
	q = q - 1
	# Main loop
	t = 0
	T = Tmax
	while T>Tmin:
		# Cooling
		t += 1
		T = Tmax*exp(-t/tau)
		'''
		# Update the visualization every 100 moves
		if t%100==0:
		l.pos = r
		'''
		# Choose two cities to swap and make sure they are distinct
		i,j = randrange(1,N),randrange(1,N)
		while i==j:
			i,j = randrange(1,N),randrange(1,N)

		# Swap them and calculate the change in distance
		oldD = D
		r[i,0],r[j,0] = r[j,0],r[i,0]
		r[i,1],r[j,1] = r[j,1],r[i,1]
		D = distance()
		deltaD = D - oldD
	    # If the move is rejected, swap them back again
		print q, f(q), D
		if deltaD > 0:
			if (((1-q)/f(q))*(deltaD/T))<=1 and random()>(1 - ((1-q)/f(q))*(deltaD/T))**(1.0/(1-q)):
				r[i,0],r[j,0] = r[j,0],r[i,0]
				r[i,1],r[j,1] = r[j,1],r[i,1]
				D = oldD	
			if (((1-q)/f(q))*(deltaD/T))>1:
				r[i,0],r[j,0] = r[j,0],r[i,0]
				r[i,1],r[j,1] = r[j,1],r[i,1]
				D = oldD
		y.append(D)
		qp.append(q)

plot(qp,y)
savefig("graf.png")
grid()
show()



