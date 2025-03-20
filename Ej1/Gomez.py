import sys
"""
Ejercicio1. Calculadora básica con clases
Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números
Incluye un constructor que inicialice los dos números como atributos.
"""
    
class Calculadora:
   
    def __init__(self):
        self.a = float(input("Introduzca un número: "))
        self.b = float(input("Introduzca otro número: "))

    def suma(self):
        return round((self.a + self.b),2)
        
    def resta(self):
        return round((self.a - self.b),2)
    
    def multiplicacion(self):
        return round((self.a * self.b),2)
    
    def division(self):
        return round((self.a / self.b),2)

calculo1 = Calculadora() 

def calcular():

    while True:

        print("\nMenú")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        operacion = input("Introduce la operacion a realizar: ")

        if operacion == "1":
            print(calculo1.suma())
        elif operacion == "2":
            print(calculo1.resta())
        elif operacion == "3":
            print(calculo1.multiplicacion())
        elif operacion == "4":
            print(calculo1.division())
        elif operacion == "5":
            print("Saliendo del programa...")
            sys.exit()


       
calcular()

if __name__ == "__main__":
    Calculadora()
    calcular()