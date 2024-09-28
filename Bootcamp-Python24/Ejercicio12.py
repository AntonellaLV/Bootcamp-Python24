# Definir la función que verifica si un número es par
def es_par(numero):
    """
    Verifica si un número es par o impar.
    
    :param numero: El número a verificar.
    :return: True si el número es par, False si es impar.
    """
    return numero % 2 == 0

# Solicitar al usuario un número
numero = int(input("Ingrese un número: "))

# Llamar a la función y mostrar si es par o impar
if es_par(numero):
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")