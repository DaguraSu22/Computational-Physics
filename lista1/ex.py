t = 0
dt = 0.4
while t <= 1.2:
	print t
	t = t + dt
	print 'dt=%.16E\nt=%.16E' % (dt, t)
	print 't <= 1.2: %g' % (t <= 1.2)
	
