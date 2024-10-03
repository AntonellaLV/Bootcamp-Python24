# 6. Listar archivos en un directorio:
# Si tienes varios archivos de logs y deseas listarlos:

import os

directorio = r'C:\Bootcamp-Python24\Bootcamp-Python24\Archivo-log'

# Crear el directorio si no existe
if not os.path.exists(directorio):
    os.makedirs(directorio)
    print(f'Directorio creado: {directorio}')
else:
    print(f'El directorio ya existe: {directorio}')

# Verificar si el directorio existe
if os.path.isdir(directorio):
    for archivo in os.listdir(directorio):
        if archivo.endswith(".log"):
            print(f'Archivo de log encontrado: {archivo}')
else:
    print(f'El directorio {directorio} no es válido o no existe.')
