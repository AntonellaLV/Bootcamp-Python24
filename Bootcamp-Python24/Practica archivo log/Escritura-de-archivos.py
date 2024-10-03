# 2. Escritura de archivos:
# Si deseas escribir o agregar más datos al archivo de logs:

import os

file_path = '/c/Bootcamp-Python24/Bootcamp-Python24/Practicas 2/http_access_200304.log'

# Verifica si el archivo existe antes de escribir
if os.path.exists(file_path):
    with open(file_path, 'a') as f:  # 'a' para modo de agregar
        f.write('Nuevo dato de log\n')
else:
    print(f'El archivo {file_path} no existe')