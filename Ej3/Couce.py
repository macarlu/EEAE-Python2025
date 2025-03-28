class Numeros:
     
     def __init__(self,enteros): #Siempre hay que poner el constructor de la clase
          
          self.lista = enteros

     def buscar_pares(self):#Metodo para buscar los pares en una lista dada

          pares = []
          for numero in self.lista:
               if numero % 2 == 0:
                    pares.append(numero)
          return pares
     
     def buscar_impares(self):
          impares = []
          for numero in self.lista:
               if numero % 2 != 0:
                    impares.append(numero)
          return impares

        
unidades = Numeros([0,1,2,3,4,5,6,7,8,9,10])
hasta_20 = Numeros([11,12,13,14,15,16,17,18,19,20])
hasta_30 = Numeros([21,22,23,24,25,26,27,28,29,30])
hasta_1000 = Numeros([101,373,422,584,658,799,981,990,997])


print(unidades.buscar_pares())
print(unidades.buscar_impares())
print(hasta_20.buscar_pares())
print(hasta_20.buscar_impares())
print(hasta_30.buscar_pares())
print(hasta_30.buscar_impares())
