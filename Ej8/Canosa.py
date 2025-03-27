'''Diseña una clase Validador con un atributo para una contraseña.
Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.'''
class Validador:
    def __init__(self, password):
        self.contraseña =password
    def verifica (self):
        longitud = len(self.contraseña) >= 8
        mayúscula = any (c.isupper() for c in self.contraseña)
        número = any (c.isdigit() for c in self.contraseña)
        if longitud and mayúscula and número:
            return "contraseña correcta"
        else:
            return "contraseña incorrecta"

password= input ("introduzca una contraseña que contenga al menos 8 caracteres, una mayúscula y un número: ")
Logon1 = Validador(password)
print (Logon1.verifica())
