import math
#metodo de newton em python

def funcao(x):
    return x**4 - 4*x**2 + 4

def derivada(x):
    return 4*x**3 - 8*x


x0 = 1.5 #chute incial
tol = 1e-2
cp = 10000000

while cp >= tol:
    x = x0 - (funcao(x0)/derivada(x0))
    cp = abs(funcao(x))
    print("x0: {}, x: {}, f(x): {}".format(x0,x,funcao(x)))
    x0 = x

