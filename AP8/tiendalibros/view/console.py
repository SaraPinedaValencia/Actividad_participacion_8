import sys

from AP8.tiendalibros.modelo.tienda_libros import TiendaLibros


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def retirar_libro_de_carrito_de_compras(self):
        isbn_usuario = input("Por favor indique el isbn del libro que va a retirar del carrito: ")
        self.tienda_libros.retirar_item_de_carrito(isbn_usuario)
        print("El libro fue retirado exitosamente")

    def agregar_libro_a_carrito_de_compras(self):
        isbn_usuario = input("Por favor indique el isbn del libro que va a agregar del carrito: ")
        cantidad = int(input("Por favor indique la cantidad que desea llevar: "))
        for isbn in self.tienda_libros.catalogo.keys():
            if isbn == isbn_usuario:
                for libro in self.tienda_libros.catalogo.values():
                    self.tienda_libros.agregar_libro_a_carrito(libro, cantidad)

    def adicionar_un_libro_a_catalogo(self):
        isbn= input("Por favor indique el isbn del libro que va a agregar del carrito: ")
        titulo = input("Por favor indique la cantidad que desea llevar: ")
        precio = float(input("Por favor indique el isbn del libro que va a agregar del carrito: "))
        existencias = int(input("Por favor indique la cantidad que desea llevar: "))
        self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
