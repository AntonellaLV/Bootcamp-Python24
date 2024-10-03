class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        return (self.lado1 * (self.lado1 * (3 ** 0.5) / 2)) / 2

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"


triangulo = Triangulo(2, 3, 1)

print("\n**********************************")
print("El perímetro es:", triangulo.perimetro())
print("El área es:", triangulo.area())
print("El tipo de triángulo es:", triangulo.tipo_triangulo())
print("**********************************")
