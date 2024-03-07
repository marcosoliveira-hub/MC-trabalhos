import math
import matplotlib.pyplot as plt

SQRT_2 = 1.41421356237309584880

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
    x_values = []
    y_values = []

    # Chute inicial
    Xo = A / 2.0
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
    pass


    

def newton_raphson_sqrt2(A, P):
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


A = 16
P = 1e-5

x_values, y_values, iter_count_nr = newton_raphson_sqrt(A, P)
real_sqrt = math.sqrt(A)
x1_values, y1_values, iter_count_s = newton_raphson_sqrt2(A, P)

plt.plot(range(len(x_values)), [real_sqrt] * len(x_values), label='Raiz Quadrada Real', linestyle='--')
plt.plot(range(len(x_values)), x_values, marker='o', label='Estimativa de Newton-Raphson')
plt.xlabel('Iteração')
plt.ylabel('Valor')
plt.title('Comparação entre a Raiz Quadrada Real e as Estimativas de Newton-Raphson')
plt.legend()
plt.grid(True)
plt.show()


plt.bar(['Newton-Raphson', 'my_sqrt'], [iter_count_nr, iter_count_s])
plt.xlabel('Método')
plt.ylabel('Número de iterações')
plt.title('Número de iterações para cada método')
plt.show()
