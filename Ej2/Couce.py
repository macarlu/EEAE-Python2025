def contar_palabras(): 

   texto = input("Introduzca un texto:")#El texto ya lo tomo como argumento de la funcion
   contador = 1
   for letra in texto:
       if letra == " ":
         contador = contador + 1
         continue
   return contador


class Texto:

   def __init__ (self,texto):

      self.texto = texto
      
   def contar_palabras(self):

      contador = 1
      for letra in self.texto:
         if letra == " ":
            contador = contador + 1
            continue
      return (f"La frase tiene: {contador} palabras")

   def guardar_palabras(self):

      return (self.texto) 


texto1 = Texto("Este es un texto para practicar")

print(texto1.contar_palabras())

print(texto1.guardar_palabras())

