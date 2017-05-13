from numpy import array, empty, zeros, sqrt, dot

def qr_fact(A):
	N = len(A)
	# B = Q and C = R
	B = zeros([N,N], float)
	C = zeros([N,N], float) 
	u = zeros([N,N], float)	# Auxiliar matrix 
	
	# Allocating the Q matrix
	for i in range (N):
		if i==0:
			u[:,i] = A[:,i]
			B[:,i] = u[:,i]/sqrt(u[:,i].dot(u[:,i]))
		else:
			u[:,i] = A[:,i]
			for j in range (i):
					u[:,i] += - B[:,j].dot(A[:,i])*B[:,j]
			B[:,i] = u[:,i]/sqrt(u[:,i].dot(u[:,i]))
	
	# Allocating the R matrix
	for i in range(N):
		for j in range(N):
			if j>=i:
				C[i,j] = A[:,j].dot(B[:,i])
	return (B,C)

# An example
X = array([[1,4,8,4],
       	   [4,2,3,7],
           [8,3,6,9],
           [4,7,9,2]],float)
Q = zeros([len(X),len(X)],float)
R = zeros([len(X),len(X)],float)

Q, R = qr_fact(X)
print Q
print R
print dot(Q,R)