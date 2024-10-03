# Leer un archivo de texto:

# Tarea 1: Leer un archivo de texto
try:
    with open('registro.txt', 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:\n", contenido)
except FileNotFoundError:
    print("El archivo 'registro.txt' no fue encontrado.")

# Explicación: Este programa abre el archivo datos.txt en modo lectura ('r'),
# lee su contenido con read() y lo imprime.
# Usa with para abrir el archivo, lo que asegura que se cierre automáticamente al terminar.
# Si el archivo no se encuentra, se maneja la excepción FileNotFoundError.