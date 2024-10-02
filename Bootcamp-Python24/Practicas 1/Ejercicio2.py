# Solicitar la edad del usuario
edad = int(input("Ingresa tu edad: "))

# Verificar si la persona puede votar
if edad >= 18:
    print("Eres mayor de 18 años, puedes votar.")
else:
    print("No puedes votar, debes ser mayor de 18 años.")
