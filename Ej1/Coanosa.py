class Calculadora:
    def __init__(self,x,y):
        self.a = x
        self.b= y
    def suma (self):
        self.adicion = self.a + self.b
        return self.adicion
    def restar (self):
        self.menos = self.a - self.b
        return self.menos
    def multiplica (self):
        self.producto = self.a * self.b
        return self.producto
    def divide (self):
        self.division = self.a / self.b
        return self.division
calculadora1 = Calculadora(1,3)
print (calculadora1.suma())
print (calculadora1.restar ())
print (calculadora1.multiplica())
print (calculadora1.divide())
