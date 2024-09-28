# Inicializar un diccionario vacío para almacenar nombres y edades
personas = {}

# Bucle para pedir nombres y edades al usuario hasta que desee detenerse
while True:
    # Solicitar el nombre y la edad de la persona
    nombre = input("Ingrese el nombre de la persona (o 'salir' para terminar): ").strip()
    
    if nombre.lower() == 'salir':
        break  # Terminar el bucle si el usuario escribe 'salir'
    
    try:
        edad = int(input(f"Ingrese la edad de {nombre}: "))
    except ValueError:
        print("Edad no válida, por favor ingrese un número entero.")
        continue
    
    # Almacenar en el diccionario
    personas[nombre] = edad

# Imprimir los datos en formato tabular
print("\nDatos de las personas ingresadas:")
print(f"{'Nombre':<15} {'Edad':<5}")
print("-" * 20)
for nombre, edad in personas.items():
    print(f"{nombre:<15} {edad:<5}")

# Calcular y mostrar el promedio de edad
if personas:
    promedio_edad = sum(personas.values()) / len(personas)
    print(f"\nEl promedio de edad es: {promedio_edad:.2f}")
else:
    print("No se ingresaron datos.")