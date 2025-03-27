'''Escribe una clase Dado que simule tirar un dado de 6 caras (usando random).
Incluye un método para tirar el dado y otro para mostrar el resultado.
EXTRA: tipos de dados (d2, d4Añade un selector de , d6, d8, d10, d12, d20)'''
import random
class Dado:
    def __init__(self):
        self.lados = 6
    def set_tirar (self):
        self.tirada = random.randint (1, self.lados)
    def get_resultado (self):
        return self.tirada
def seleccionar_dado():
    print("Selecciona un tipo de dado:")
    print("1. d2")
    print("2. d4")
    print("3. d6")
    print("4. d8")
    print("5. d10")
    print("6. d12")
    print("7. d20")
    opcion = int(input("Introduce el número de tu selección: "))

    dados_disponibles = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 20}
    return dados_disponibles.get(opcion, 6)  # Por defecto devuelve un d6 si la opción no es válida

dado= Dado()
dado.set_tirar()
print (dado.get_resultado())
lados = seleccionar_dado()
dado = Dado(lados)
dado.set_tirar()
print(f"Has seleccionado un dado de {lados} caras.")
print(f"El resultado del lanzamiento del dado es: {dado.get_resultado()}")
