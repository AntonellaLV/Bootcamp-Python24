# Lista de temperaturas en grados Celsius
temperaturas_celsius = [0, 20, 37, 100]

# Convertir a Fahrenheit utilizando map y una función lambda
temperaturas_fahrenheit = list(map(lambda c: c * 9/5 + 32, temperaturas_celsius))

# Imprimir la lista resultante en grados Fahrenheit
print("Temperaturas en Fahrenheit:", temperaturas_fahrenheit)