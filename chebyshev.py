import math
import matplotlib.pyplot as plt
import numpy as np

def sen_taylor(x):
    y = x * x
    return x * (1 + y * ((-1/6) + y * ((1/120) + y * ((-1/5040) + y * ((1/362880) + y * (-1/39916800))))))

def cos_taylor(x):
    y = x * x
    return 1 + y * ((-1/2) + y * ((1/24) + y * ((-1/720) + y * ((1/40320) + y * ((-1/3628800) + y * (1/479001600))))))

def sen(x):
    if (x >= (-1 * (math.pi/4)) and (x <= (math.pi/4))):
        return sen_taylor(x)
    else:
       k = math.ceil((x - (math.pi/4)) / math.pi/2)
       r = x - (k * (math.pi/2))

       match (abs(k) % 4):
              case 0:
                return sen_taylor(r)
              case 1:
                return cos_taylor(r)
              case 2:
                return -sen_taylor(r)
              case 3:
                return -cos_taylor(r)
              case _:
                return "Erro"

def cos(x):
    if (x >= (- math.pi/4)) and (x <= (math.pi/4)):
        return cos_taylor(x)
    else:
       k = math.ceil((x - (math.pi/4)) / math.pi/2)
       r = x - (k * (math.pi/2))
       match (abs(k) % 4):
              case 0:
                return cos_taylor(r)
              case 1:
                return -sen_taylor(r)
              case 2:
                return -cos_taylor(r)
              case 3:
                return sen_taylor(r)
              case _:
                return "Erro"



def erro_sin(x):
    return abs(math.sin(x) - sen(x))

def erro_cos(x):
    return abs(math.cos(x) - cos(x))


# Intervalo de valores de x
x_values = np.linspace(-1, 1, 1000)

# Calculando os erros para seno e cosseno
sen_errors = [erro_sin(x) for x in x_values]
cos_errors = [erro_cos(x) for x in x_values]

# Plotando os gráficos
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x_values, sen_errors, label='Erro do Seno')
plt.title('Erro do Seno')
plt.xlabel('x')
plt.ylabel('Erro')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_values, cos_errors, label='Erro do Cosseno', color='orange')
plt.title('Erro do Cosseno')
plt.xlabel('x')
plt.ylabel('Erro')
plt.legend()

plt.tight_layout()
plt.show()
