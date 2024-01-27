import math
import matplotlib.pyplot as plt 

SQRT_2 = 1.41421356237309584880

# Trabalho Matemática Computacional

# Grupo:
# - Marcos Vinicius de Oliveira RA: 124408
# - Guilherme Frare Clemente RA: 124349


# Trabalho da raiz quadrada


# Função que calcula a raiz quadrada de um número x
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


# Função que calcula o erro entre a raiz quadrada calculada e a raiz quadrada da biblioteca math
def erro(x):
    return math.fabs(math.sqrt(x) - my_sqrt(x))


# Função que calcula o erro entre a raiz quadrada calculada e a raiz quadrada da biblioteca math
def numbers(start, end, step):
    number = []
    n = start
    while n < end:
        number.append(n)
        n += step
    return number

# Função principal
# Plota o gráfico do erro em função do número
def main():
    numeros = numbers(0, 5, 0.05)
    erros = [erro(x) for x in numeros]
    plt.plot(numeros, erros)
    plt.show()

main() 