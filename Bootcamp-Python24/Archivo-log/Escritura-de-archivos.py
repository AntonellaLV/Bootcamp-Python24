# 2. Escritura de archivos:
# Si deseas escribir o agregar más datos al archivo de logs:

import os

# Corrige la ruta del archivo de logs
file_path = r'C:\Bootcamp-Python24\Bootcamp-Python24\Practica archivo log'

try:
    # Verifica si el archivo existe antes de escribir
    if os.path.exists(file_path):
        with open(file_path, 'a') as f:  # 'a' para modo de agregar
            f.write("Este es un mensaje de prueba.\n")
        print("Escritura completada con éxito.")
    else:
        print(f'El archivo {file_path} no existe')
except PermissionError:
    print(f"No se tiene permiso para escribir en el archivo: {file_path}")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")

# Verifica si el archivo existe antes de escribir
if os.path.exists(file_path):
    with open(file_path, 'a') as f:  # 'a' para modo de agregar
        f.write('Nuevo dato de log\n')
else:
    print(f'El archivo {file_path} no existe')