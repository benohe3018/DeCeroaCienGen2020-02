#Definiendo una variable
nombre1 = "Hayde"
nombre2 = "Paola"
nombre3 = "Daniel"

#Ejemplo programación estructurada
print("Hola "+ nombre1)
print("Hola "+ nombre2)
print("Hola "+ nombre3)

#Ejemplo programación modular

#Definiendo una función
def saludo(nombre):
    print("Hola "+nombre)

#Llamando a mi función
saludo(nombre1)
saludo(nombre2)
saludo(nombre3)

#Ejemplo programación orientada a objetos

class Saludo():
    def _init_(self):
        "Estoy instanciando un objeto de la clase saludo/n"
    def saludo1(self, nombre):
        print("Hola "+ nombre)

#Instanciar un objeto de clase saludo

saludo2 = Saludo()
saludo2.saludo1(nombre1)
saludo2.saludo1(nombre2)
saludo2.saludo1(nombre3)
