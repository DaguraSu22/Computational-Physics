from math import sqrt, tan, log10

# Declaracao das constantes
m = 9.1094e-31       # Massa do eletron
w = 1.0000e-9	
h = 6.582119514e-16  # Constant de Plank/2pi
V = 20.1
#Tolerancia
epsilon = 0.001
# Funcoes
def y_1(x):
	# Niveis pares
	return tan(sqrt((w*w*m*x/(2*h*h*1.6e-19)))) - sqrt((V - x)/x)
def y_2(x):
	# Niveis impares
	return tan(sqrt((w*w*m*x/(2*h*h*1.6e-19)))) + sqrt(x/(V - x))
# Procedimento da biseccao
def bisec(f, a, b, e):
	nmax = int(round((log10(b-a) - log10(2*e))/log10(2))+1)
	fa = f(a)
	fb = f(b)
	if fa*fb > 0:
		print "Nao ha raizes nesse intervalo!"
	error = b - a
	for i in range (nmax):
		error = error/2
		c = a + error
		fc = f(c)
		if abs(error)<e:
			return c
		if fa*fc < 0:
			b = c
			fb = fc
		else:
			a = c
# Exemplo para o primeiro nivel de energia 
print bisec(y_1, 0.3, 0.4, epsilon)  
