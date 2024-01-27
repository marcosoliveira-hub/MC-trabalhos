# Trabalho Matemática Computacional

# Grupo:
# - Marcos Vinicius de Oliveira RA: 124408
# - Guilherme Frare Clemente RA: 124349

# Exponenciação pelo método de Bailey

import math
import matplotlib.pyplot as plt 

EULER = math.e

def recursiva(base, k):
    if k < 0:
        return recursiva(1/base, -k)
    elif k == 0:
        return 1
    elif k == 1:
        return base
    elif k % 2 == 0:
        return recursiva(base, (k/2)) ** 2
    else:
        return base * recursiva(base, k-1)

def bailey(x):
    
    n = math.ceil(x/math.log(2) - 0.5)
    r = (x - n * math.log(2)) / 256

    if n >= 0:
        c1 = 1 << n
    else:
        c1 = 1 / (1 << -n)
    
    er = 1 + r * (1 + r * ((1/2) + r * ((1/6) + (1/24) * r)))

    return c1 * (er ** 256)


def my_exp(base, x):

    x_inteira = int(x)
    x_fracionada = x - x_inteira
    return recursiva(base, x_inteira) * bailey(x_fracionada)
    
    

def error(x):
    return abs(math.exp(x) - my_exp(EULER, x))


def numbers(start, end, step):
    number = []
    n = start
    while n < end:
        number.append(n)
        n += step
    return number


def main():
    numeros = numbers(-5, 5, 0.05)
    erros = [error(x) for x in numeros]
    plt.plot(numeros, erros)
    plt.show()


main()