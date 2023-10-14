from libro_error import LibroError
from libro import  Libro

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, libro: Libro, cantidad_a_comprar: int):
        self.cantidad_a_comprar: int = cantidad_a_comprar
        super().__init__(libro)

    def __str__(self):
        return f"El libro con titulo: {self.libro.titulo} e isbn: {self.libro.isbn} no tiene suficientes existencias para realizar la compra: {self.cantidad_a_comprar}, existencias: {self.libro.existencias}"