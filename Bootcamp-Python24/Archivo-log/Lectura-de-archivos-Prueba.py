# 1. Lectura de archivos:
# Para leer el archivo que contiene estos datos de logs,
# usar el siguiente enfoque con os y open:

import os

# Cambia esta ruta al archivo específico que deseas leer
file_path = r'C:\Bootcamp-Python24\Bootcamp-Python24\Archivo-log\http_access_200304.log'

# Verifica si el archivo existe
if os.path.exists(file_path):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                print(line.strip())  # Lee y muestra cada línea
    except PermissionError:
        print(f'No tienes permiso para acceder al archivo: {file_path}')
    except Exception as e:
        print(f'Ocurrió un error al abrir el archivo: {e}')
else:
    print(f'El archivo {file_path} no existe')
