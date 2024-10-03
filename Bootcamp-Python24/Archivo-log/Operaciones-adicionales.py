# 4. Operaciones adicionales (renombrar, eliminar, etc.):
# Puedes usar os para realizar operaciones en el archivo, como renombrar o eliminar.
import os

# Rutas de los archivos
archivo_original = r'C:\Bootcamp-Python24\Bootcamp-Python24\Archivo-log'
archivo_renombrado = r'C:\ruta\a\archivo_renombrado.log'

# Renombrar un archivo
try:
    os.rename(archivo_original, archivo_renombrado)
    print(f'Archivo renombrado de {archivo_original} a {archivo_renombrado}')
except FileNotFoundError:
    print(f'No se pudo encontrar el archivo: {archivo_original}')
except PermissionError:
    print(f'No tienes permiso para renombrar el archivo: {archivo_original}')
except Exception as e:
    print(f'Ocurrió un error al renombrar el archivo: {e}')

# Eliminar un archivo (asegúrate de que el archivo ya no se necesite)
try:
    os.remove(archivo_renombrado)  # Elimina el archivo renombrado
    print(f'Archivo eliminado: {archivo_renombrado}')
except FileNotFoundError:
    print(f'No se pudo encontrar el archivo: {archivo_renombrado}')
except PermissionError:
    print(f'No tienes permiso para eliminar el archivo: {archivo_renombrado}')
except Exception as e:
    print(f'Ocurrió un error al eliminar el archivo: {e}')
