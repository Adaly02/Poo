# Superclase
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        print("Este animal hace un sonido.")

    def describir(self):
        print(f"Soy un {self.__class__.__name__}, me llamo {self.nombre} y tengo {self.edad} años.")

# Subclase Perro que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau, guau!")

# Subclase Gato que hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):
        print("Miau, miau!")

# Crear instancias de las subclases
mi_perro = Perro("Max", 5)
mi_gato = Gato("Luna", 3)

# Usar métodos de la superclase y subclases
mi_perro.describir()  # Heredado de Animal
mi_perro.hacer_sonido()  # Sobrescrito en Perro

mi_gato.describir()  # Heredado de Animal
mi_gato.hacer_sonido()  # Sobrescrito en Gato
