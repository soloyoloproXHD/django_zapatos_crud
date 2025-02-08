from .models import Usuario, Zapato
from abc import ABC, abstractmethod

#CREATORS
class Usuario_Creator(ABC): #Clase abstracta
    @abstractmethod
    def create(self, email: str, password: str):
        pass

class Zapato_Creator(ABC): #Clase abstracta
    @abstractmethod
    def create(self, marca: str, modelo: str, talla: int, color: str, precio: float, stock: int, descripcion: str, estado: bool): 
        pass

#CONCRETE CREATORS
class Usuario_Factory(Usuario_Creator): #Clase concreta
    def create(self, email: str, password: str) -> Usuario:
        return Usuario.objects.create(email=email, password=password) #Se crea el objeto Usuario

class Zapato_Factory(Zapato_Creator): #Clase concreta
    def create(self, marca: str, modelo: str, talla: int, color: str, precio: float, stock: int, descripcion: str, estado: bool = True) -> Zapato:
        return Zapato.objects.create( #Se crea el objeto Zapato
            marca=marca,
            modelo=modelo,
            talla=talla,
            color=color,
            precio=precio,
            stock=stock,
            descripcion=descripcion,
            estado=estado
        )
