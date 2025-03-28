class Conversor_temperatura:
    
    def __init__(self,temperatura_base):
        self.temp = temperatura_base

    def celsius_fahrenheit(self):
        temperatura_fahrenheit = (self.temp * 9/5) + 32
        return temperatura_fahrenheit
    
    def fahrenheit_celsius(self):
        temperatura_celsius = (self.temp - 32) * 9/5
        return temperatura_celsius
    
    def celsius_kelvin(self):
        temperatura_kelvin = self.temp + 273
        return temperatura_kelvin
    

conversor_1 = Conversor_temperatura(25)
print ("25º C a Fahrenheit: ", conversor_1.celsius_fahrenheit())#Pongo el metodo apropiado

conversor_2 = Conversor_temperatura(98.6)
print ("108.4º F a Celsius:", conversor_2.fahrenheit_celsius())

conversor_3 = Conversor_temperatura(27)
print ("27º C a Kelvin:",conversor_3.celsius_kelvin())
