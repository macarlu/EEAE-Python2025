'''Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa.
Usa un constructor para inicializar una temperatura base.'''
class ConversorTemperatura:
    def __init__(self, base):
        self.tbase = base
    def De_Celsius_a_Fah (self):
        self.tcelsius = (self.tbase*9/5)+32
        return self.tcelsius
    def De_Fah_a_Cel (self):
        self.tfah = (self.tcelsius-32)*5/9
        return  self.tfah
Estamos = ConversorTemperatura(16)
print ("la temperatura en grados Fahrenheit es de", Estamos.De_Celsius_a_Fah())
print ("la temperatura en grados Celsius es de", Estamos.De_Fah_a_Cel())
