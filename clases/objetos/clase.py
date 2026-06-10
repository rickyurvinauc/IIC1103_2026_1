class Persona:

    def __init__(self, nombre, apellido, edad): # atributos necesarios cuando se crea el obejto
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        texto = self.nombre+" "+self.apellido+" edad: "+str(self.edad)

        return texto

# creacion del objeto
ricardo = Persona("Ricardo","Urvina", 30)
ingrid = Persona("Ingrid","Medina", 31)
print(ricardo)
print(ingrid)

