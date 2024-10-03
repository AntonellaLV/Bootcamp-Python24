# 5. Buscar una cadena específica:
# Si quieres buscar un término específico en el archivo, puedes hacerlo fácilmente:

import os

term = 'GET /archive/2003/04/03/typo_pop.shtml'
file_path = r'C:\Bootcamp-Python24\Bootcamp-Python24\Archivo.log'

# Verifica si el archivo existe, si no, lo crea
if not os.path.exists(file_path):
    with open(file_path, 'w') as f:  # 'w' crea el archivo si no existe
        f.write('Este es un log de prueba.\n')
        f.write('GET /archive/2003/04/03/typo_pop.shtml\n')  # Agrega una línea que contiene el término
        print(f'Archivo creado: {file_path}')

# Ahora busca el término en el archivo
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if term in line:
                print(f'Término encontrado: {line}')
else:
    print(f'El archivo {file_path} no existe.')
