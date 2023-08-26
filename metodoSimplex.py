import numpy as np
from scipy.optimize import linprog

# Coeficientes de la función objetivo a maximizar: c^T * x
c = np.array([-2, -3])

# Coeficientes de las restricciones: A * x <= b
A = np.array([[1, 1],
              [2, 1],
              [1, -1]])

# Lado derecho de las restricciones
b = np.array([5, 8, 1])

# Rangos de las variables (en este caso, todas son >= 0)
x_bounds = [(0, None)] * len(c)

# Resuelve el problema utilizando el solucionador 'highs'
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

if result.success:
    print("Solución encontrada:")
    print("Valor óptimo =", -result.fun)  # Minimización -> Multiplicamos por -1 para maximización
    print("Variables =", result.x)
else:
    print("El problema no tiene solución óptima.")
