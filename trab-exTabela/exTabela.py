# Trabalho Matemática Computacional

# Grupo:
# - Marcos Vinicius de Oliveira RA: 124408
# - Guilherme Frare Clemente RA: 124349

# Exponenciação pelo método LUT (Look Up Table)

import math
import matplotlib.pyplot as plt


EULER = math.e

# Tabela LUT
lut = {
    5.5452: 256,
    2.7726: 16,
    1.3863: 4,
    0.6931: 2,
    0.4055: 1.5,
    0.2231: 1.25,
    0.1178: 1.125,
    0.0606: 1.0625,
    0.0308: 1.03125,
    0.0155: 1.015625,
    0.0078: 1.0078125
    # Continue a lista conforme necessário
}


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
    
def LUT(x, lut):
    y = 1
    pos_tabela = 0
    while pos_tabela < len(lut) and x > 0:
        keys = list(lut.keys())
        value = list(lut.values())
        if keys[pos_tabela] > x:
            pos_tabela += 1
        else:
            x -= keys[pos_tabela]
            y *= value[pos_tabela]
    
    return (1 + x) * y
    

def my_exp(base, x):
    x_inteira = int(x)
    x_fracionada = x - x_inteira
    return recursiva(base, x_inteira) * LUT(x_fracionada, lut)


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
