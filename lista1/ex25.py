from numpy import loadtxt
values = loadtxt("values.txt", float)
mean = sum(values)/len(values)
print mean
