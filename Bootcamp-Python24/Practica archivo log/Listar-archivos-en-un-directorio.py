# 6. Listar archivos en un directorio:
# Si tienes varios archivos de logs y deseas listarlos:

import os

directorio = '/c/Bootcamp-Python24/Bootcamp-Python24/Practicas 2/http_access_200304.log'
for archivo in os.listdir(directorio):
    if archivo.endswith(".log"):
        print(f'Archivo de log encontrado: {archivo}')