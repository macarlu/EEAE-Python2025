class Estudiante:

    def __init__ (self, name,age,mark):

        self.nombre = name
        self.edad = age
        self.nota = mark

    def set_nombre(self,name): #Setter del nombre

        self.nombre = name
        
    def get_nombre(self,name): #Getter del nombre

        self.nombre = name
        return self.nombre

    def set_edad (self,age): #Setter de la edad

        self.edad = age
        
    def get_edad (self,age):#Getter de la edad

        self.edad = age
        return self.edad
    
    def set_nota (self,mark):

        self.nota = mark

    def get_nota (self,mark):

        self.nota = mark
        return self.nota
    
    def nota_aprobado (self):

        if self.nota >= 6:
            return "Aprobado"
        else:
            return "Suspenso"
    

estudiante_1 = Estudiante("Pepe",28,5.95)
print (estudiante_1.nota_aprobado())

estudiante_2 = Estudiante("Jaime",35,6.2)
print (estudiante_2.get_nota(6))

estudiante_3 = Estudiante("Carlos",23,7)
print(estudiante_3.nota_aprobado())
