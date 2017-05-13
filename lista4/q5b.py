from numpy import linspace,abs
from math import exp, log

# Declaracao das constantes
G = 6.674e-11 # Constante de gravitacao universal
M = 5.974e24 # Massa do Sol
m = 7.348e22 # Massa da Lua
R = 3.844e8 # Distancia entre o centro da lua e o centro da Terra
w = 2.662e-6 # Velocidade angular da rotacao da Lua em torno do Sol

def f(r):
    y = w*w*r**5 - 2*w*w*R*r**4 + w*w*R*R*r**3 + G*m*r*r 
    y = y - G*M*r*r + 2*G*M*R*r - G*M*R*R
    return y

def f1(r):
    y = 5*w*w*r**4 - 8*w*w*R*r**3 + 3*w*w*R*R*r**2 + 2*G*m*r - 2*G*M*r + 2*G*M*R
    return y

def f2(r):
    y = 20*w*w*r**3 - 24*w*w*R*r**2 + 6*w*w*R*R*r + 2*G*m - 2*G*M
    return y

erro = 0.1
x1 = 0
precisao = 1e-3

while(erro>=precisao):
    x1, x2 = x1 - f(x1)/f1(x1),x1
    erro = abs(x2-x1)
    erro = -erro*erro*f2(x1)/(2*f1(x1))
                
print x1
