class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # Método para calcular el perímetro
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    # Método para calcular el área usando la fórmula de Herón
    def area(self):
        semi_perimetro = self.perimetro() / 2
        area = (semi_perimetro * (semi_perimetro - self.lado1) * (semi_perimetro - self.lado2) * (semi_perimetro - self.lado3)) ** 0.5
        return area

    # Método para determinar el tipo de triángulo según sus lados
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    # Verificación de si es un triángulo válido
    def es_valido(self):
        # La suma de dos lados debe ser mayor que el tercer lado en todo triángulo
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)

# Ejemplo de uso
lado1 = 3
lado2 = 4
lado3 = 5

triangulo = Triangulo(lado1, lado2, lado3)

if triangulo.es_valido():
    print(f"Perímetro: {triangulo.perimetro()}")
    print(f"Área: {triangulo.area():.2f}")
    print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}")
else:
    print("Los lados ingresados no forman un triángulo válido.")