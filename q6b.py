from numpy import array, empty, zeros, sqrt, dot
def qr_fact(A):	# QR factorization
	N = len(A)
	B = zeros([N,N], float)	# B = Q 
	C = zeros([N,N], float) # C = R
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
# An example
X = array([[1,4,8,4],
       	   [4,2,3,7],
           [8,3,6,9],
           [4,7,9,2]],float)
Q, R = zeros([len(X),len(X)],float),zeros([len(X),len(X)],float)
Q, R = qr_fact(X)
print Q,"\n",R,"\n",dot(Q,R)