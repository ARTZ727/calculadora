import matplotlib.pyplot as plt
import numpy as np

def multiplicação(num1, num2):
    return num1 * num2
def Divisão(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return ('não é possivel dividir por zero')
def soma(num1, num2):
    return num1 + num2
def menos(num1, num2):
    return num1 - num2
def potenciação(num1, num2):
    return num1 ** num2
def fatorial(num):
    if num < 0:
        return 'não é possivel calcular'
    elif num == 0:
        return 1
    else:
        resultado = 1
        for x in range(1, num + 1):
            resultado*= x
        return resultado
def eq_segundo_grau(a, b, c):

    delta = (b**2 - 4 * a * c)
    

    if delta >= 0:
        numerador1 = -b + delta**0.5
        numerador2 = -b - delta**0.5
        if a == 0:
            return f'\nImpossivel dividor por zero \n {numerador1} / ({a} x 2) --> {numerador1} / 0\n{numerador2} / ({a} x 2) --> {numerador2} / 0'
        resposta1 = numerador1/(a*2)
        resposta2 = numerador2/(a*2)
        resposta = (f'\nx1 = {resposta1} \nx2 = {resposta2}')
        return resposta
    else:
        return f'\nImpossivel realizar a operação, delta é menor que zero\n{b}² - 4 x {a} x {c} = {delta}'


def plot_fatorial(n):
    x = list(range(n + 1))
    y = [fatorial(i) for i in x]
    plt.plot(x, y)
    plt.title('fatorial')
    plt.xlabel('numero')
    plt.ylabel('fatorial')
    plt.grid(True)
    plt.show()
def plot_linear(a, b):
    listax = np.linspace(-10,10, 50)
    listay = a*listax + b
    plt.plot(listax, listay)
    plt.title(f'função linear de {a}x + {b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
def plot_exponencial(a):
    listax = np.arange(-2, 2.1, 0.1)
    listay = a**listax
    plt.plot(listax, listay)
    plt.title(f'exponecial de {a}^x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
def plot_raiz(a):
    listax = np.arange(0, 4.1, 0.005)
    listay = listax**(1/a)
    plt.plot(listax, listay)
    plt.title(f'raiz de x por {a}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
def plot_quadratica(a, b, c):
    listax = np.linspace(-10, 10, 50)
    listay = a * listax ** 2 + b * listax + c
    plt.plot(listax, listay)
    plt.title('Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()  
