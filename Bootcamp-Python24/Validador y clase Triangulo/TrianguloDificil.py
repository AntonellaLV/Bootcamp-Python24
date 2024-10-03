class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        s = self.perimetro() / 2
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        return area if area > 0 else 0  # Triángulos degenerados tienen área 0

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    def es_valido(self):
        if not (self.lado1 > 0 and self.lado2 > 0 and self.lado3 > 0):
            raise ValueError("Los lados deben ser mayores que 0.")
        
        if not (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1):
            return False
        return True

print("\n**********************************")
try:
    triangulo = Triangulo(3, 4, 5)

    if triangulo.es_valido():
        print(f"Perímetro: {triangulo.perimetro()}")
        print(f"Área: {triangulo.area():.2f}")
        print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}")
    else:
        print("Los lados no forman un triángulo válido.")

except ValueError as e:
    print(f"Error: {e}")
print("**********************************")