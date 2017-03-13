from math import exp 

m = input("Entre com o valor de x: ")
s = input("Entre com o valor de s: ")
while s<=0:
	print("O valor de s precisa ser maior que 0. Por favor, tente novamente.")
	s = input("Entre com o valor de s: ")
x = input("Entre com o valor de x: ")

print "m = ", m
print "s = ", s
print "x = ", x
print "f(x) = ", exp(-1/2*((x-m)**2/s))
