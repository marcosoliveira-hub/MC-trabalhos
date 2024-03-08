import math
import matplotlib.pyplot as plt
import numpy as np


def sen_taylor(x):
    y = x * x
    return x * (
        1
        + y
        * (
            (-1 / 6)
            + y
            * ((1 / 120) + y * ((-1 / 5040) + y * ((1 / 362880) + y * (-1 / 39916800))))
        )
    )


def cos_taylor(x):
    y = x * x
    return 1 + y * (
        (-1 / 2)
        + y
        * (
            (1 / 24)
            + y
            * (
                (-1 / 720)
                + y * ((1 / 40320) + y * ((-1 / 3628800) + y * (1 / 479001600)))
            )
        )
    )


def sen(x):
    while x > 2 * math.pi:
        x -= 2 * math.pi

    while x < -2 * math.pi:
        x += 2 * math.pi

    if x >= (-1 * (math.pi) / 4) and x <= (math.pi / 4):
        return sen_taylor(x)
    else:
        k = math.ceil((x - (math.pi / 4)) / math.pi / 2)
        r = x - (k * (math.pi / 2))

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
    while x > 2 * math.pi:
        x -= 2 * math.pi

    while x < -2 * math.pi:
        x += 2 * math.pi
    if x >= (-1 * (math.pi) / 4) and x <= (math.pi / 4):
        return cos_taylor(x)
    else:
        k = math.ceil((x - (math.pi / 4)) / math.pi / 2)
        r = x - (k * (math.pi / 2))
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
x_values = np.linspace(-8 * math.pi, 8 * math.pi, 1000)

# Calculando os erros para seno e cosseno
sen_errors = [erro_sin(x) for x in x_values]
cos_errors = [erro_cos(x) for x in x_values]

# Plotando os gráficos
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x_values, sen_errors, label="Erro do Seno")
plt.title("Erro do Seno")
plt.xlabel("x")
plt.ylabel("Erro")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_values, cos_errors, label="Erro do Cosseno", color="orange")
plt.title("Erro do Cosseno")
plt.xlabel("x")
plt.ylabel("Erro")
plt.legend()

plt.tight_layout()
plt.show()


# T11 = 1024x11 - 2816x9 + 2816x7 - 1232x5 + 220x3 - 11x
# Dividir o polinomio de chebyshev por 1024, para conseguirmos ter o monico

# sen(x) = sen(x)11 - (Polinomio monico de chebyshev de grau 11)
# sen(x) = sen(x)11 - ( an * tn(x)/2^n - 1)

# an e o termo de grau 11 do sen(x)11
# Nesse caso seria o -1/11!
