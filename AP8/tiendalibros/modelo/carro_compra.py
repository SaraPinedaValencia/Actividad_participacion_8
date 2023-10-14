from item_compra import ItemCompra
from libro import Libro

class CarroCompras:
    def __init__(self):
        self.items: list[ItemCompra] = []

    def agregar_item(self, libro: Libro, cantidad: int) -> ItemCompra:
        item = ItemCompra(libro, cantidad)
        self.items.append(item)
        return item

    def calcular_total(self) -> float:
        total = 0
        for item in self.items:
            total += item.calcular_subtotal()
        return total

    def quitar_item(self, isbn: str):
        self.items = [item for item in self.items if item.libro.isbn != isbn]

