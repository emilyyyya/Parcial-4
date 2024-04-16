import numpy as np

# Definir la función cuya raíz queremos encontrar
def f(x):
    return x**3 - 2*x - 5

# Método de bisección
def biseccion(a, b, tol):
    iteraciones = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c, iteraciones
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteraciones += 1
    return (a + b) / 2, iteraciones

# Método de la secante
def secante(x0, x1, tol, max_iter):
    iteraciones = 0
    while iteraciones < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2, iteraciones
        x0 = x1
        x1 = x2
        iteraciones += 1
    return x2, iteraciones

# Método de Newton-Raphson
def newton_raphson(x0, tol, max_iter):
    iteraciones = 0
    while iteraciones < max_iter:
        x1 = x0 - f(x0) / derivada_f(x0)
        if abs(x1 - x0) < tol:
            return x1, iteraciones
        x0 = x1
        iteraciones += 1
    return x1, iteraciones

# Derivada de la función
def derivada_f(x):
    return 3 * x**2 - 2

# Definir los límites y la tolerancia
a = 1
b = 3
tol = 1e-6
x0 = 3
x1 = 2
max_iter = 1000

# Ejecutar los métodos
raiz_biseccion, iteraciones_biseccion = biseccion(a, b, tol)
raiz_secante, iteraciones_secante = secante(x0, x1, tol, max_iter)
raiz_newton, iteraciones_newton = newton_raphson(x0, tol, max_iter)

# Imprimir resultados
print("Método de bisección:")
print("Raíz:", raiz_biseccion)
print("Iteraciones necesarias:", iteraciones_biseccion)

print("\nMétodo de la secante:")
print("Raíz:", raiz_secante)
print("Iteraciones necesarias:", iteraciones_secante)

print("\nMétodo de Newton-Raphson:")
print("Raíz:", raiz_newton)
print("Iteraciones necesarias:", iteraciones_newton)

