Documentación del Código de Programación Lineal con Simplex y SciPy //  Francisco Gomez -- 28.182.231 -- Universidad Jose Antonio Paez -- Docente: Maria Valentina Garcia Contreras. 

Descripción:
Este código resuelve un problema de programación lineal utilizando el método Simplex a través de la librería SciPy. Se busca maximizar una función objetivo sujeta a restricciones lineales.

Requisitos:
- Python 3.x instalado en el sistema.
- La librería NumPy y SciPy deben estar instaladas. Si no están instaladas, puedes instalarlas usando 'pip install numpy scipy'.

Parámetros y Variables:
- c: Coeficientes de la función objetivo a maximizar. Representa la contribución de cada variable a la función objetivo.
- A: Matriz de coeficientes de las restricciones. Cada fila representa una restricción, y cada columna representa una variable.
- b: Vector de lados derecho de las restricciones. Indica los límites de cada restricción.
- x_bounds: Lista de tuplas que definen los rangos de las variables. Cada tupla representa el rango de una variable (por ejemplo, (0, None) significa que la variable es no negativa).

Resultado:
El código utiliza el solucionador 'highs' de SciPy para resolver el problema de programación lineal. Si se encuentra una solución óptima, se imprime el valor óptimo de la función objetivo y las asignaciones óptimas de las variables. Si no se encuentra una solución óptima, se muestra un mensaje indicando que el problema no tiene solución.

Nota:
El solucionador 'highs' se utiliza en lugar del método 'simplex' debido a que el último está marcado como obsoleto en versiones futuras de SciPy.

Uso:
1. Asegúrate de tener instaladas las librerías NumPy y SciPy.
2. Reemplaza los valores de 'c', 'A' y 'b' con los coeficientes y restricciones de tu problema.
3. Ejecuta el código en un entorno Python.

Importante:
Este código es una guía básica para resolver problemas de programación lineal utilizando el método Simplex. Los problemas específicos pueden requerir ajustes en los datos y las restricciones para obtener resultados precisos y significativos.
