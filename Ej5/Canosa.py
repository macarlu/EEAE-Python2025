'''Crea una clase Estudiante con atributos para nombre, edad y calificación.
Implementa métodos getter y setter, y un método que determine si el estudiante aprobó (calificación mayor o igual a 6).'''
class Estudiante:
    def __init__(self, name, age, mark):
        self.nombre = name
        self.edad = age
        self.nota = mark
    def set_nombre(self, name):
        self.nombre = name
    def get_nombre (self):
        return self.nombre
    def set_edad (self, age):
        self.edad = age
    def get_edad (self):
        return self.edad
    def set_nota (self,mark):
        self.nota = mark
    def get_nota(self):
        return self.nota
    def calificar (self):
        if self.nota >= 6:
            return ("aprobado")
        else:
            return ("supenso")
Estudiante1 = Estudiante ("Pedro", 44, 4)
print ("El nombre del estudiante es", Estudiante1.get_nombre (),",", "tiene la edad de", Estudiante1.get_edad(),"," "y ha sacado una nota de", Estudiante1.get_nota(), "con lo que está", Estudiante1.calificar())
