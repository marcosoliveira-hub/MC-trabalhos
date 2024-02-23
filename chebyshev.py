import math
import matplotlib.pyplot as plt
import numpy as np


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


def sen_taylor(x):
    y = x * x
    return x * (1 - y * (1/fatorial(3) + y * (1/fatorial(5) - y * (1/fatorial(7) + y * (1/fatorial(9) - y * (1/fatorial(11)))))))

def cos_taylor(x):
    y = x * x
    return 1 - y * (1/fatorial(2) + y * (1/fatorial(4) - y * (1/fatorial(6) + y * (1/fatorial(8) - y * (1/fatorial(10)) + y * (1/fatorial(12))))))
    

def sen(x):
    if (x > (-1 * (math.pi/4)) and (x < (math.pi/4))):
        return sen_taylor(x)
    else:
       k = math.ceil((x - (math.pi/4)) / math.pi/2)
       r = x - k * (math.pi/2)

       if (abs(k) % 4) == 0:
           return sen_taylor(r)
       elif (abs(k) % 4) == 1:
            return cos_taylor(r)
       elif (abs(k) % 4) == 2:
            return -sen_taylor(r)
       elif (abs(k) % 4) == 3:
            return -cos_taylor(r)
       
def cos(x):
    if (x > (- math.pi/4)) and (x < (math.pi/4)):
        return cos_taylor(x)
    else:
       k = math.ceil((x - (math.pi/4)) / math.pi/2)
       r = x - k * (math.pi/2)

       if (abs(k) % 4) == 0:
           return cos_taylor(r)
       elif (abs(k) % 4) == 1:
            return -sen_taylor(r)
       elif (abs(k) % 4) == 2:
            return -cos_taylor(r)
       elif (abs(k) % 4) == 3:
            return -sen_taylor(r)



def erro_sin(x):
    return abs(sen(x) - math.sin(x))

def erro_cos(x):
    return abs(cos(x) - math.cos(x))


x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Calcule os erros para cada x
erro_sen = [erro_sin(i) for i in x]
erro_cos = [erro_cos(i) for i in x]

# Crie o plot
plt.figure(figsize=(10, 6))

# Plot erro do seno
plt.plot(x, erro_sen, label='Erro do Seno')

# Plot erro do cosseno
plt.plot(x, erro_cos, label='Erro do Cosseno')

# Adicione um título e rótulos aos eixos
plt.title('Erro do Seno e Cosseno')
plt.xlabel('x')
plt.ylabel('Erro')

# Adicione uma legenda
plt.legend()

# Adicione linhas de grade
plt.grid(True)

# Mostre o plot
plt.show()