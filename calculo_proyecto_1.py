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

def prueba(f,x,x0,n):  #Funcion de prueba de polinomio de taylor
   
    poli=polinomio_taylor(f,x0,n)
    print("Valor Aproximado: ",poli(x))
    print("      Valor Real: ",f(x))
    print("  Error Relativo: ", f(x)-poli(x))


#Newton-Raphson
def newton_raphson(f, x, ER, N):
    """
    Implementa el Algoritmo de Newton-Raphson y retorna la aproximación de la
    raiz.
            Variables:
    f: función de variable real f(x).
    x: aproximación inicial.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """
    i = 1; err = 1; xi = None
    
    while i <= N and ER < err:
        xi = x - (f(x)/derivada(f)(x))
        err = er(x, err)
        print("Iteración:", i, "Aproximación:", xi, "Error:", err)
        i += 1
    return xi


er = lambda a,b: math.fabs((a-b)/a)


if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.
    print("Resultado Polinomio de taylor:")
    f1=lambda x: math.exp(25*x**3 - 6*x**2 + 7*x - 88)
    prueba(f1,2,1,3)
    #Prueba de Newton-Raphson
    f = lambda x: math.exp(-x) - math.log(x)
    print("Resultado newton-raphson:")
    print(newton_raphson(f, 0.1, 0.1, 10))
