# Paso 1: Solicitar al usuario una lista de números
numeros = list(map(int, input("Ingresa una lista de números separados por espacios: ").split()))

# Paso 2: Función para calcular el cuadrado de cada número usando map
def calcular_cuadrados(numeros):
    return list(map(lambda x: x**2, numeros))

# Paso 3: Función para filtrar solo los números pares usando filter
def filtrar_pares(numeros):
    return list(filter(lambda x: x % 2 == 0, numeros))

# Paso 4: Función que devuelve los números cuadrados y pares en una lista por comprensión
def cuadrados_pares(numeros):
    # Calcular cuadrados
    cuadrados = calcular_cuadrados(numeros)
    # Filtrar pares de los cuadrados
    pares = filtrar_pares(cuadrados)
    # Devolver resultado en una lista por comprensión
    return [num for num in pares]

# Llamar a la función y mostrar el resultado
resultado = cuadrados_pares(numeros)
print("Cuadrados de los números pares:", resultado)