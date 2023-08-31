#Programación Orientada a Objetos (POO) y funciones
#Javascript / Java

#Funciones
def saludo(nombre):
    print(f'Hola {nombre}')

saludo('Pedro')

class Persona:

    #Constructor
    def __init__(self, nombre, edad, oficio):
        self.nombre = nombre
        self.edad = edad
        self.oficio = oficio

    def saludar(self):
        print(f'Hola {self.nombre}')

    #Getters get obtener
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_oficio(self):
        return self.oficio
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad
    
persona1 = Persona('Pablo', 18, 'Mesero')
persona2 = Persona('Juan', 20, 'Desarrollador')

arreglo_personas = [persona1, persona2]

print(arreglo_personas)
