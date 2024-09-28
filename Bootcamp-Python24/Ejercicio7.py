# Crear dos conjuntos de números
conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {4, 5, 6, 7, 8}

# Operación de unión (unión de todos los elementos de ambos conjuntos)
union = conjunto_1.union(conjunto_2)

# Operación de intersección (elementos comunes a ambos conjuntos)
interseccion = conjunto_1.intersection(conjunto_2)

# Operación de diferencia (elementos que están en el conjunto_1 pero no en conjunto_2)
diferencia = conjunto_1.difference(conjunto_2)

# Imprimir los resultados de las operaciones
print(f"Unión de conjuntos: {union}")
print(f"Intersección de conjuntos: {interseccion}")
print(f"Diferencia (conjunto_1 - conjunto_2): {diferencia}")