# Tarea 2: Leer archivo línea por línea
try:
    with open('datos.txt', 'r') as archivo:
        for linea in archivo:
            print(linea.strip())  # Imprimir cada línea sin espacios adicionales
except FileNotFoundError:
    print("El archivo 'datos.txt' no fue encontrado.")

# Explicación: El archivo se lee línea por línea utilizando un bucle for.
# Se usa strip() para eliminar espacios y saltos de línea innecesarios.