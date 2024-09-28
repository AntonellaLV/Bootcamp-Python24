# Crear un diccionario con nombres y edades
personas = {
    "Juan": 25,
    "María": 30,
    "Carlos": 22
}

# Solicitar al usuario el nombre de la persona cuya edad desea consultar
nombre = input("Introduce el nombre de la persona para obtener su edad: ")

# Verificar si la persona está en el diccionario
if nombre in personas:
    # Imprimir la edad de la persona
    print(f"La edad de {nombre} es: {personas[nombre]} años")
else:
    print(f"No se encontró a la persona '{nombre}' en el diccionario.")