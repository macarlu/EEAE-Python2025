'''Crea una clase Numeros con un atributo que sea una lista de enteros.
Incluye un método que devuelva solo los números pares de esa lista.'''
class Números:
    def __init__(self, list):
        self.enteros = list
    def pares(self):
        return [num for num in self.enteros if num % 2 == 0]

# Ejemplo de uso
numeros = Números([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(numeros.pares())  # Salida: [2, 4, 6, 8, 10]
