import math
import matplotlib.pyplot as plt

# Função para calcular a raiz quadrada usando o método de Newton-Raphson
def newton_raphson_sqrt(A, P):
    x_values = []
    y_values = []

    # Chute inicial
    Xo = A / 2.0
    x1 = Xo

    erro = float('inf')

    while erro > P:
        x_values.append(x1)
        y_values.append(abs(math.sqrt(A) - x1))

        # Atualização da estimativa usando a fórmula de Newton-Raphson
        x0 = x1
        x1 = 0.5 * (x0 + A / x0)
        erro = abs(x1 - x0)

    return x_values, y_values

# Valor de A (número dentro da raiz quadrada)
A = 10
# Precisão desejada
P = 1e-5

# Calcula as estimativas de raiz quadrada usando o método de Newton-Raphson
x_values, y_values = newton_raphson_sqrt(A, P)

# Calcula a raiz quadrada real de A
real_sqrt = math.sqrt(A)

# Plotagem do gráfico das diferenças entre a raiz quadrada real e as estimativas de raiz quadrada em cada iteração
plt.plot(range(len(x_values)), [real_sqrt] * len(x_values), label='Raiz Quadrada Real', linestyle='--')
plt.plot(range(len(x_values)), x_values, marker='o', label='Estimativa de Newton-Raphson')
plt.xlabel('Iteração')
plt.ylabel('Valor')
plt.title('Comparação entre a Raiz Quadrada Real e as Estimativas de Newton-Raphson')
plt.legend()
plt.grid(True)
plt.show()
