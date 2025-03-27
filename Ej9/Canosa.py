'''Crea una clase Notas con una lista de calificaciones como atributo.
Implementa un método que calcule el promedio y otro que devuelva la nota más alta. 
Añade manejo de excepciones para evitar notas inferiores a 0 o superiores a 10.'''
class Notas:
    def __init__(self, marks):
        if any(nota < 0 or nota > 10 for nota in marks):
            raise ValueError("Las calificaciones deben estar entre 0 y 10.")
        self.calificaciones = marks
    def Nota_media (self):
        return sum (self.calificaciones)/ len (self.calificaciones)
    def NotaAlta (self):
        ordenada = sorted(self.calificaciones, reverse=True)
        return  ordenada [0]
try:
    marks = Notas([4, 6, 11, 3, 9, 6, 7])
#marks = Notas([4,6,8,3,9,6,7])
    print (f"el promedio de las calificaciones es:{marks.Nota_media()}")
    print (f"la nota más alta es:{marks.NotaAlta()}")
except ValueError as e:
    print(f"Error: {e}")
