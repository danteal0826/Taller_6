import numpy as np

A = np.array([[3, 1],[1, 2]])

valores_propios, vectores_propios = np.linalg.eig(A)

print("Valores propios:")
print(valores_propios)
print("\nVectores propios:")
print(vectores_propios)