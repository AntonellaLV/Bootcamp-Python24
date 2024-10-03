# Tarea 4: Cerrar archivos correctamente
nombres = ["Ana", "Luis", "Carlos", "Marta"]

archivo = open('registro.txt', 'w')
for nombre in nombres:
    archivo.write(nombre + "\n")
archivo.close()

print("Nombres escritos y archivo 'registro.txt' cerrado correctamente.")

# Explicación: Aquí se abre el archivo sin with, pero se cierra manualmente utilizando archivo.close().
# Asegura que el archivo se cierre correctamente.