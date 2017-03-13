from numpy import loadtxt, array
from math import log, exp 
values = loadtxt("values.txt", float)
logs = array(map(log,values), float)
geometric = exp(sum(logs)/len(logs))
print geometric

