import matplotlib.pyplot as plt
import numpy as np
import math as m

# Objetivo: computar seno e cosseno com a garantia de alcance
# de precisão de 10^-11, com x E [-2pi, 2pi].

# Reduzir o número de multiplicações por meio da aplicação das séries 
# telescópicas de Chebychev (séries econômicas).
    
#valores para reduzir o valor do argumento
c = m.pi/2
x_max = 0.7853981633974483 #45° ou Pi/4


def fat(x):
    if x == 0:
        return 1
    else:
        return x * fat(x-1)


def angle_to_rad(x):
    return x * m.pi / 180


def sin_taylor(x):
    if x<=x_max and x>=-x_max:
        return x - pow(x,3)/fat(3) + pow(x,5)/fat(5) - pow(x,7)/fat(7) + pow(x,9)/fat(9) - pow(x,11)/fat(11)
    else:
        return cos_taylor(x - c)


#seno com uma redução, utilizando séries telescópicas
def sin(x): #P(9)
    if x<=x_max and x>=-x_max:
        y = x*x
        return x*(3715891199/3715891200 + y * (-30965759/185794560 + y * (276479/33177600 + y * (-2879/14515200 + y * (13/4838400)))))
    else:
        return cos(x - c)


#seno com duas reduções, utilizando séries telescópicas
def sin2(x): #P(7)
    if x<=x_max and x>=-x_max:
        y = x*x
        return x*(116121589/116121600 + y * (-6193105/37158912 + y * (19343/2322432 + y * (-319/1658880))))
    else:
        return cos(x - c)


def cos_taylor(x):
    if x<=x_max and x>=-x_max:
        return 1 - pow(x,2)/fat(2) + pow(x,4)/fat(4) - pow(x,6)/fat(6) + pow(x,8)/fat(8) - pow(x,10)/fat(10) + pow(x,12)/fat(12)
    else:
        k = m.ceil((x - x_max)/c)
        xr = x - k*c
        if k%4 == 0:
            return cos_taylor(xr)
        elif k%4 == 1:
            return -sin_taylor(xr)
        elif k%4 == 2:
            return -cos_taylor(xr)
        else:
            return sin_taylor(xr)

# cos com uma redução, utilizando séries telescópicas
def cos(x): #~P(10) 
    if x<=x_max and x>=-x_max:
        y = x*x 
        return 980995276801/980995276800 + y * (-6812467201/13624934400 + y * (48660481/1167851520 + y * (-380161/273715200 + y * (503/20275200 + y * (-1/3548160)))))
    else:
        k = m.ceil((x - x_max)/c)
        xr = x - k*c #reduzindo o valor do argumento
        if k%4 == 0:
            return cos(xr)
        elif k%4 == 1:
            return -sin(xr)
        elif k%4 == 2:
            return -cos(xr)
        else:
            return sin(xr)


def cos2(x): #~P(8) 
    if x<=x_max and x>=-x_max:
        y = x*x 
        return 12740198393/12740198400 + y * (-309657583/619315200 + y * (30965597/743178240 + y * (-138179/99532800 + y * (311/12902400))))
    else:
        k = m.ceil((x - x_max)/c)
        xr = x - k*c #reduzindo o valor do argumento
        if k%4 == 0:
            return cos(xr)
        elif k%4 == 1:
            return -sin(xr)
        elif k%4 == 2:
            return -cos(xr)
        else:
            return sin(xr)

        
def plot_values():
    x = []
    y = []
    z = []

    escolha = int(input("Escolha como deseja realizar o Calculo:\n 1 - Taylor\n 2 - Chebyshev - uma redução\n 3 - Chebyshev - duas reduções\nSua escolha: "))

    n = -360

    if escolha == 1:
        while n <= 360:
            x.append(n)
            y.append(abs(m.sin(angle_to_rad(n)) - sin_taylor(angle_to_rad(n))))
            z.append(abs(m.cos(angle_to_rad(n)) - cos_taylor(angle_to_rad(n))))

            n += 1
    elif escolha == 2:
        while n <= 360:
            x.append(n)
            y.append(abs(sin_taylor(angle_to_rad(n)) - sin(angle_to_rad(n))))
            z.append(abs(cos_taylor(angle_to_rad(n)) - cos(angle_to_rad(n))))

            n += 1
    elif escolha == 3:
        while n <= 360:
            x.append(n)
            y.append(abs(sin_taylor(angle_to_rad(n)) - sin2(angle_to_rad(n))))
            z.append(abs(cos_taylor(angle_to_rad(n)) - cos2(angle_to_rad(n))))

            n += 1
    
    return x,y,z


x, y, z = plot_values()


plt.figure(figsize=(10, 5))


# # plt.subplot(3, 1, 1)
plt.plot(x, y, color='blue')
plt.plot(x, z, color='red')
plt.title('Gráfico do Cálculo do Cosseno e Seno')
plt.xlabel('Ângulo (°)')    
plt.ylabel('Erro')
plt.legend(['Seno', 'Cosseno'])

plt.show()