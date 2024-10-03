# 2. Clase Triángulo con métodos de Perímetro y Área

import math

class Triangulo:
    def __init__(self, a, b, c):
        # Validamos si las medidas forman un triángulo válido
        if self.es_triangulo_valido(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("Las medidas no forman un triángulo válido.")

    def es_triangulo_valido(self, a, b, c):
        # Las medidas deben cumplir la desigualdad del triángulo
        return a + b > c and a + c > b and b + c > a

    def perimetro(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Ejemplo de uso
triangulo = Triangulo(3, 4, 5)

print(f"Perímetro del triángulo: {triangulo.perimetro()}")
print(f"Área del triángulo: {triangulo.area()}")