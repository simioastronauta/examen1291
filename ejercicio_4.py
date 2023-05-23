"""
4 - Escribe un programa que genere una matriz de tamaño 4 x 4
con números enteros aleatorios en el rango del 1 al 10. A continuación, realiza las siguientes operaciones:

    • Calcula la suma de todos los elementos de la matriz.
    • Calcula el promedio de todos los elementos de la matriz.
    • Encuentra el valor máximo y mínimo de la matriz.
    • Imprime la matriz original, la suma de cada columna y el resultado de todas las operaciones anteriores.
"""
import numpy as np
import random
matris = np.random.randint(1,10,size=(4,4))
print(matris)

suma = matris.sum()
print(f"Suma {suma}")
media = matris.mean()
print(f"Media {media}")
masimo = matris.max()
minimo = matris.min()
columnas = sum(matris)
print(f"Maximo {masimo}")
print(f"minimo {minimo}")
print(columnas)

