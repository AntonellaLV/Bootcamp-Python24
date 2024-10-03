import os

# Tarea 5: Operaciones con archivos usando os

# Crear una carpeta llamada 'mi_directorio'
if not os.path.exists('mi_directorio'):
    os.mkdir('mi_directorio')
    print("Directorio 'mi_directorio' creado.")
else:
    print("El directorio 'mi_directorio' ya existe.")

# Listar el contenido del directorio actual
contenido = os.listdir('.')
print("\nContenido del directorio actual:")
for item in contenido:
    print(item)

# Eliminar el archivo 'registro.txt'
if os.path.exists('registro.txt'):
    os.remove('registro.txt')
    print("\nArchivo 'registro.txt' eliminado.")
else:
    print("\nEl archivo 'registro.txt' no existe.")

# Explicación: Crear un directorio: Usa os.mkdir() para crear la carpeta mi_directorio si no existe.
# Listar contenido: Utiliza os.listdir() para listar los archivos y carpetas en el directorio actual.
# Eliminar archivo: Usa os.remove() para eliminar registro.txt si existe.