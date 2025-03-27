'''Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo.'''
#código inicial:
'''Cadena = input("Introduzca un refrán popular: ")
contador = 1
for i in Cadena:
    if i == " ":
        contador += 1
print (f"El refrán contiene {contador} palabras")'''
def cuenta_palabras(Cadena):
    contador = 1
    for i in Cadena:
        if i == " ":
            contador += 1
    return contador
#refran =input("Introduzca un refrán popular: ")
#numero_palabras = cuenta_palabras(refran)
print (f"El refrán contiene {cuenta_palabras(input("Introduzca un refrán popular: "))} palabras")
#ahora la paso a clase:
class Texto:
    def __init__(self):
        pass
    def cuenta_palabras(self, chain):
        contador = 1
        self.cadena = chain
        for i in chain:
            if i == " ":
                contador += 1
        return contador
    
chain1 = Texto ()
chain1.cuenta_palabras(print (f"El refrán contiene {(input("Introduzca un refrán popular: "))} palabras"))
