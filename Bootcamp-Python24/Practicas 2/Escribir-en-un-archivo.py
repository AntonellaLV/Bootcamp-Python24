# Tarea 3: Escribir en un archivo
nombres = ["Ana", "Luis", "Carlos", "Marta"]

with open('registro.txt', 'w') as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")

print("Nombres escritos en 'registro.txt'.")

# Explicación: Este programa abre registro.txt en modo escritura ('w').
# Escribe cada nombre en la lista nombres en el archivo, y añade un salto de línea después de cada nombre.
# Usamos el contexto with para cerrar el archivo automáticamente.