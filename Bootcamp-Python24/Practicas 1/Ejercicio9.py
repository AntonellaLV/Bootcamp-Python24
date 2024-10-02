# Tupla de números
numeros = (3, 56, 12, 89, 7, 21, 34)

# Inicializar las variables para almacenar el valor máximo y mínimo
maximo = numeros[0]
minimo = numeros[0]

# Recorrer la tupla para encontrar el máximo y mínimo
for numero in numeros:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

# Imprimir los resultados
print(f"El valor más grande es: {maximo}")
print(f"El valor más pequeño es: {minimo}")