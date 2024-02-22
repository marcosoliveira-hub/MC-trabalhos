import math 
import matplotlib.pyplot as plt

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def chebyshev_series(n, x):
    result = 0
    for k in range(n + 1):
        coefficient = (-1)**k * (x**(2*k))
        coefficient /= fatorial(2*k)
        result += coefficient
    return result

def chebyshev_economic_series(n, x):
    tn_x = chebyshev_series(n, x)
    an = (-1)**n / (2**n - 1)
    pn_minus_1_x = tn_x - an * (chebyshev_series(n, x) / (2**(n-1) - 1))
    return pn_minus_1_x

def reduce_argument(x, K):
    return x - K * math.floor(x / K)

def sin_chebyshev(x, n):
    reduced_x = reduce_argument(x, math.pi / 4)
    result = chebyshev_economic_series(n, reduced_x)
    if abs(reduced_x) == math.pi / 4:
        return math.sin(reduced_x)
    else:
        k = math.floor(x / (math.pi / 4))
        if abs(k) % 4 == 1 or abs(k) % 4 == 2:
            result *= -1
        return result

def cos_chebyshev(x, n):
    reduced_x = reduce_argument(x, math.pi / 4)
    result = chebyshev_economic_series(n, reduced_x)
    if abs(reduced_x) == math.pi / 4:
        return math.cos(reduced_x)
    else:
        k = math.floor(x / (math.pi / 4))
        if abs(k) % 4 == 1 or abs(k) % 4 == 2:
            result *= -1
        return result

def sin_chebyshev_2x(x, n):
    reduced_x = reduce_argument(reduce_argument(x, math.pi / 4), math.pi / 4)
    result = chebyshev_economic_series(n, reduced_x)
    if abs(reduced_x) == math.pi / 4:
        return math.sin(reduced_x)
    else:
        k = math.floor(x / (math.pi / 4))
        if abs(k) % 4 == 1 or abs(k) % 4 == 2:
            result *= -1
        return result

def cos_chebyshev_2x(x, n):
    reduced_x = reduce_argument(reduce_argument(x, math.pi / 4), math.pi / 4)
    result = chebyshev_economic_series(n, reduced_x)
    if abs(reduced_x) == math.pi / 4:
        return math.cos(reduced_x)
    else:
        k = math.floor(x / (math.pi / 4))
        if abs(k) % 4 == 1 or abs(k) % 4 == 2:
            result *= -1
        return result

x_values = [-2 * math.pi, -math.pi, -math.pi/2, 0, math.pi/2, math.pi, 2 * math.pi]
n = 11

for x in x_values:
    print(f"Seno de {x}: {sin_chebyshev(x, n)}")
    print(f"Cosseno de {x}: {cos_chebyshev(x, n)}")

def plot_comparative_graph(x_values, y1_values, y2_values, y3_values, title):
    plt.plot(x_values, y1_values, label="Original", color='red')
    plt.plot(x_values, y2_values, label="Reduzido 1x", color='blue')
    plt.plot(x_values, y3_values, label="Reduzido 2x", color='green')
    plt.xlabel("x")
    plt.ylabel("Valor")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

y1_values_sin = [math.sin(x) for x in x_values]
y2_values_sin = [sin_chebyshev(x, n) for x in x_values]
y3_values_sin = [sin_chebyshev_2x(x, n) for x in x_values]
plot_comparative_graph(x_values, y1_values_sin, y2_values_sin, y3_values_sin, "Comparação do Seno")

y1_values_cos = [math.cos(x) for x in x_values]
y2_values_cos = [cos_chebyshev(x, n) for x in x_values]
y3_values_cos = [cos_chebyshev_2x(x, n) for x in x_values]
plot_comparative_graph(x_values, y1_values_cos, y2_values_cos, y3_values_cos, "Comparação do Cosseno")