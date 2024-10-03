# 1. Validador

class ValidadorDNI:
    def __init__(self, lista_documentos):
        self.lista_documentos = lista_documentos
        self.lista_documentos_validos = []
        self.lista_documentos_invalidos = []

    def validar_documento(self, documento):
        if self.todo_es_un_numerico(documento) and self.rango_valido(documento):
            self.lista_documentos_validos.append(documento)
        else:
            self.lista_documentos_invalidos.append(documento)

    def todo_es_un_numerico(self, valor):
        # Verificar si el valor contiene solo dígitos
        return valor.isdigit()

    def rango_valido(self, valor):
        # Un rango típico para DNI en Argentina es entre 1000000 y 99999999
        dni = int(valor)
        return 1000000 <= dni <= 99999999

    def obtener_dni_validos(self):
        return self.lista_documentos_validos

    def obtener_dni_invalidos(self):
        return self.lista_documentos_invalidos

# Ejemplo de uso:
lista_dnis = ["12345678", "87654321", "abc123", "987654321"]
validador = ValidadorDNI(lista_dnis)

for dni in lista_dnis:
    validador.validar_documento(dni)

print("DNIs válidos:", validador.obtener_dni_validos())
print("DNIs inválidos:", validador.obtener_dni_invalidos())