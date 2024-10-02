# Lista de tuplas (nombre, edad)
personas = [("Juan", 25), ("Ana", 30), ("Pedro", 22), ("Lucía", 28)]

# Usar sorted con una expresión lambda para ordenar por la edad (segundo valor en la tupla)
personas_ordenadas = sorted(personas, key=lambda persona: persona[1])

# Imprimir la lista de personas ordenadas por edad
print("Personas ordenadas por edad:")
for nombre, edad in personas_ordenadas:
    print(f"{nombre}: {edad} años")