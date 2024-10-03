# 1. Lectura de archivos:
# Para leer el archivo que contiene estos datos de logs,
# usar el siguiente enfoque con os y open:

import os

# Verifica si el archivo existe
file_path = '/c/Bootcamp-Python24/Bootcamp-Python24/Practicas 2/http_access_200304.log'
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            print(line.strip())  # Lee y muestra cada línea
else:
    print(f'El archivo {file_path} no existe')