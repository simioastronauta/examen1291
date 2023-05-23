"""
1 - Crea una matriz aleatoria de 3x4 y cámbiala a una matriz de 4x3 utilizando la función "reshape".
"""
import numpy as np
import random
matris = np.random.randint(10,size=(3,4))
print(matris)
cambiada = matris.reshape((4,3))
print("si")
print(cambiada)