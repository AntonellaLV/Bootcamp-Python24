# Solicitar un número al usuario
numero = int(input("Ingresa un número para imprimir su tabla de multiplicar: "))

# Usar un bucle for para imprimir la tabla de multiplicar del número
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")