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



def erro(x):
    return math.fabs(math.sqrt(x) - my_sqrt(x))


def numbers(start, end, step):
    number = []
    n = start
    while n < end:
        number.append(n)
        n += step
    return number

def main():
    numeros = numbers(0, 5, 0.05)
    erros = [erro(x) for x in numeros]
    plt.plot(numeros, erros)
    plt.show()

main() 