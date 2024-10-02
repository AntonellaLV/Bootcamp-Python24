# Solicitar diferentes tipos de datos al usuario
texto = input("Ingresa un texto: ")  # Captura un string
entero = int(input("Ingresa un número entero: "))  # Convierte la entrada a entero
decimal = float(input("Ingresa un número decimal: "))  # Convierte la entrada a float
booleano = input("Ingresa un valor booleano (True/False): ")  # Captura un string

# Convertir el string booleano a tipo booleano
if booleano.lower() == "true":
    booleano = True
elif booleano.lower() == "false":
    booleano = False
else:
    print("Entrada inválida para booleano, valor predeterminado a False.")
    booleano = False

# Imprimir cada dato junto con su tipo
print("\nDatos ingresados y sus tipos:")
print(f"Texto: '{texto}', Tipo: {type(texto)}")
print(f"Entero: {entero}, Tipo: {type(entero)}")
print(f"Decimal: {decimal}, Tipo: {type(decimal)}")
print(f"Booleano: {booleano}, Tipo: {type(booleano)}")