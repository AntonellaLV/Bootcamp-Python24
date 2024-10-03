class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        s = self.perimetro() / 2
        return (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    def es_valido(self):
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)


triangulo = Triangulo(3, 4, 5)

print("\n**********************************")
if triangulo.es_valido():
    print(f"Perímetro: {triangulo.perimetro()}")
    print(f"Área: {triangulo.area():.2f}")
    print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}")
else:
    print("Los lados no forman un triángulo válido.")
print("**********************************")