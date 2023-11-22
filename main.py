import numpy as np

matriz = np.array([1, 2, 3, 4, 5])
print(matriz)

m2d = np.array([[1, 2, 3], [4, 5, 6]])
print(m2d)

lista = [1, 2, 3]
lista1d = np.array(lista)
print(lista1d)

lista3d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz3d = np.array(lista3d)
print(matriz3d)

#TO CREATE MATRIZ WITH CONSICUTIVE NUMBER AND DIFFERENT SHAPE
m = np.arange(15).reshape(3,5)
print(m)