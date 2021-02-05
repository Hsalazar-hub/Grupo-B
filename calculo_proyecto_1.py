#!/usr/bin/env python3
import math
"""
EJERCICIO 1: Implemente en lenguaje Python una función que aproxime mediante un Polinomio de Taylor de tercer orden centrado en x=1 para predecir f(2), siendo f(x) = 25x**3 – 6x**2 + 7x – 88. Calcule luego el error relativo de la aproximación.

EJERCICIO 2: Implemente en lenguaje Python el método de Newton-Raphson para aproximar la solución de f(x) = 0, siendo f(x) = exp(-x)-ln(x).

Escriba aqui los nombres de los integrantes del grupo:
-Hector Salazar. C.I 25967387 
-Lewis Narvaez. C.I 26087715
"""
#Taylor
def derivada(f, h = 0.01):
    """
    devuelve la función derivada de f dado un h.
        Parametros:
        f: función f(x).
        h: tamaño del paso.
    """

    def _(x):
        return (f(x + h) - f(x))/h

    return _

def polinomio_taylor(f, x0, n):
    """
    Devuelve el Polinomio de Taylor de grado n centrado en x0.
    Parametros:
        f: función f(x).
        x0: centro del polinomio.
        n: grado del polinomio.
        p:Polinomio
        d_Actual:Derivada actual
    """
    def polinomio(x):
        i=1
        p=f(x0)     #inicio del polinomio 
        while (i!=n+1):
            if (i==1):
                d_Actual=derivada(f)    #Primera derivada
                p+=d_Actual(x0) * (x-x0)    #Se agrega al polinomio la primera derivada
            else:
                d_Actual=derivada(d_Actual) #Se calculan todas las demas derivadas
                p+=( d_Actual(x0) * (x-x0)**i ) / math.factorial(i) #Se agregan al polinomio las demas iteraciones
            i+=1      
        return p
    return polinomio