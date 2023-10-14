from carro_compra import CarroCompras
from libro import Libro
from libro_existente_error import LibroExistenteError
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:
    def __init__(self):
        self.catalogo: dict[str:Libro] = {}
        self.carrito: CarroCompras = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn1: str, titulo: str, precio: float, existencias: int) -> Libro:
        for isbn in self.catalogo.keys():
            if isbn == isbn1:
                libro_existente = Libro(isbn1, titulo, precio, existencias)
                raise LibroExistenteError(libro_existente)
            else:
                libro = Libro(isbn1, titulo, precio, existencias)
                self.catalogo[isbn1] = libro
                return libro

    def agregar_libro_a_carrito(self, libro: Libro, cantidad_a_agregar: int):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro)
        elif cantidad_a_agregar > libro.existencias:
            raise ExistenciasInsuficientesError(libro)
        else:
            self.carrito.agregar_item(libro, cantidad_a_agregar)

    def retirar_item_de_carrito(self, isbn: str):
        self.carrito.quitar_item(isbn)

