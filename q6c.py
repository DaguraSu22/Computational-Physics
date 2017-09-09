from numpy import array, empty, zeros, sqrt, dot, identity
def qr_fact(A):			# QR factorization			
	N = len(A)
	# B = Q and C = R
	B = zeros([N,N], float)
	C = zeros([N,N], float) 
	u = zeros([N,N], float)	# Auxiliar matrix 
		for i in range (N):
		if i==0:
			u[:,i] = A[:,i]
			B[:,i] = u[:,i]/sqrt(u[:,i].dot(u[:,i]))
		else:
			u[:,i] = A[:,i]
			for j in range (i):
					u[:,i] += - B[:,j].dot(A[:,i])*B[:,j]
			B[:,i] = u[:,i]/sqrt(u[:,i].dot(u[:,i]))
	for i in range(N):
		for j in range(N):
			if j>=i:
				C[i,j] = A[:,j].dot(B[:,i])
	return (B,C)
def qr_alg(A,delta): 	# QR Algorithm	
	N = len(A)
	Q = zeros([N,N],float)
	R = zeros([N,N],float)
	V = identity(N)			# V is eigenvector matrix
	W = empty(N,float)		# W is eigenvalues matrix
	for i in range (N):
		for j in range(N):
			if i!=j:
				while A[i,j]>delta:
					Q, R = qr_fact(A)
					A = dot(R,Q)
					V = dot(V,Q)
	for i in range (N):
		for j in range(N):
			if i==j:
				W[i]=A[i,j]
	return (W, V)
# An example
epsilon = 1e-6 				# Accuracy
X = array([[1,4,8,4],
       	   [4,2,3,7],
           [8,3,6,9],
           [4,7,9,2]],float)
eigval = zeros([len(X),len(X)],float)
eigvec = zeros([len(X),len(X)],float)
eigval, eigvec = qr_alg(X,epsilon)
print eigval,"\n",eigvec