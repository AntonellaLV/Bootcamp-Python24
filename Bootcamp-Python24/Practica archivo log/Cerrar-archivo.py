# 3. Cerrar archivos:
# Cuando utilizas el contexto with open,
# no es necesario cerrar el archivo manualmente, ya que se cierra automáticamente.
# Si no estás usando el contexto:

f = open('/c/Bootcamp-Python24/Bootcamp-Python24/Practicas 2/http_access_200304.log', 'r')
# Algunas operaciones de lectura
f.close()  # Cierra el archivo manualmente después de su uso