import math
import matplotlib.pyplot as plt
import struct
import numpy as np


SQRT_2 = 1.41421356237309584880
P_64 = 2 ** 61
Q_64 = 2 ** 52

def my_sqrt(x):
    m, k = math.frexp(x)
    m, k  = m * 2, k - 1

    #Calcula raiz de m = 1 + f
    f = m - 1
    sqrt_f = 1 + f/2*(1 - f/(4 + 2*f))

    #calcula raiz de 2**k
    neg = False
    if k < 0:
        k = -k
        neg = True
    
    if k == 0:
        sqrt_2k = 1
    elif k == 1:
        sqrt_2k = SQRT_2
    elif k & 1 == 0:
        sqrt_2k = 1 << (k >> 1)
    elif k & 1 == 1:
        sqrt_2k = (1 << ((k - 1) >> 1)) * SQRT_2
    

    if neg:
        sqrt_2k = 1/sqrt_2k

    return sqrt_f * sqrt_2k

def newton_raphson_sqrt(A, P):
    if A == 0.0:
        return [0.0], [0.0], 0
    
    x_values = []
    y_values = []

    # Chute inicial
    Xo = calcular_chute_inicial(A)
    x1 = Xo

    erro = float('inf')
    iter_count = 0

    while erro > P:
        x_values.append(x1)
        y_values.append(abs(math.sqrt(A) - x1))
        x0 = x1
        x1 = 0.5 * (x0 + A / x0) 
        erro = abs(x1 - x0)
        iter_count += 1

    return x_values, y_values, iter_count



def calcular_chute_inicial(A):
    if A == 0.0:
        return 0.0
    
    P = P_64
    Q = Q_64

    class FloatUnion:
        def __init__(self, f):
            self.f = f
            self.x = struct.unpack('<Q', struct.pack('<d', f))[0]
    
    val = FloatUnion(A)
    val.x -= Q
    val.x >>= 1
    val.x += P

    return struct.unpack('<d', struct.pack('<Q', val.x))[0]


def newton_raphson_sqrt2(A, P):
    if A == 0.0:
        return [0.0], [0.0], 0
    
    x_values = []
    y_values = []

    # Chute inicial
    Xo = my_sqrt(A)
    x1 = Xo

    erro = float('inf')
    iter_count = 0

    while erro > P:
        x_values.append(x1)
        y_values.append(abs(math.sqrt(A) - x1))
        x0 = x1
        x1 = 0.5 * (x0 + A / x0)
        erro = abs(x1 - x0)
        iter_count += 1

    return x_values, y_values, iter_count


P = 1e-5
x = np.linspace(0, 20, 10000)
y = [newton_raphson_sqrt(x, P)[2] for x in x]
y2 = [newton_raphson_sqrt2(x, P)[2] for x in x]

plt.plot(x, y, label='Newton-Raphson')
plt.plot(x, y2, label='Newton-Raphson2')
plt.xlabel('Valor de A')
plt.ylabel('Iterações')
plt.legend()
plt.show()
