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