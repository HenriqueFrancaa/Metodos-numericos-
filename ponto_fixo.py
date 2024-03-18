import math
#metodo do ponto fixo em python

def phi(x): # e(euler) = 2.71
    return (2.71**x) - 2

def funcao(x):
    return (2.71**x) - 2 - x

x0 = -1.8
cp = 10000000
tol = 1e-7

while cp >= tol:
    x = phi(x0)
    print("x: {}, phi(x): {}, funcao(x): {}".format(x,phi(x),funcao(x)))
    x0 = x
    cp = abs(funcao(x))