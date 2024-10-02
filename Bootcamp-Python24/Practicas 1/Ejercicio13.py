# Definir la expresión lambda para calcular el cuadrado de un número
cuadrado = lambda x: x ** 2

# Lista de números para los que se calculará el cuadrado
numeros = [2, 3, 4, 5, 6]

# Usar la expresión lambda para imprimir el cuadrado de cada número
for num in numeros:
    print(f"El cuadrado de {num} es {cuadrado(num)}")