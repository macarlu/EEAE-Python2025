class Calculadora:

    def __init__(self,num1,num2):

        self.num1 = num1
        self.num2 = num2

    def suma_numeros (self):

        return self.num1 + self.num2
    
    def resta_numeros (self):

        return self.num1 - self.num2
    
    def divide_numeros (self):

        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No podemos dividir entre 0"
          
    def multiplica_numeros (self):

        return self.num1 * self.num2
    
calculadora1 = Calculadora(4,5)
calculadora2 = Calculadora(7,8)
calculadora3 = Calculadora(40,20)

print("La suma de los numeros es:",calculadora1.suma_numeros())  #Despues de metodo parentesis
print("La resta de los numeros es:",calculadora1.resta_numeros())

print("El producto de los numeros es",calculadora2.multiplica_numeros())
print("El cociente de los numeros es:",calculadora2.divide_numeros())

print("El cociente de los numeros es:",calculadora3.divide_numeros())






