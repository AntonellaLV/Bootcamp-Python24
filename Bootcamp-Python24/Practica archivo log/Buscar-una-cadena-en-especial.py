# 5. Buscar una cadena específica:
# Si quieres buscar un término específico en el archivo, puedes hacerlo fácilmente:

term = 'GET /archive/2003/04/03/typo_pop.shtml'
file_path = '/c/Bootcamp-Python24/Bootcamp-Python24/Practicas 2/http_access_200304.log'

with open(file_path, 'r') as f:
    for line in f:
        if term in line:
            print(f'Término encontrado: {line}')