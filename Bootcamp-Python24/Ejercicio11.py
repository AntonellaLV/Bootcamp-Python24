# Definir la función que calcula el área del rectángulo
def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo.
    
    :param largo: Largo del rectángulo.
    :param ancho: Ancho del rectángulo.
    :return: Área del rectángulo (largo * ancho).
    """
    return largo * ancho

# Solicitar al usuario las dimensiones del rectángulo
largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

# Llamar a la función y mostrar el resultado
area = calcular_area_rectangulo(largo, ancho)
print(f"El área del rectángulo es: {area}")