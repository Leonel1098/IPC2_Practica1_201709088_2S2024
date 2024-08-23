from Auto import Auto
from Cliente import Cliente

class Compra:

    contador_id = 1
    def __init__(self,cliente):
        self.id += Compra.contador_id
        Compra.contador_id += 1
        self.cliente = cliente
        self.lista_productos = []
        self.costo_total = float

    def agregar_producto(self, producto, seguro):
        seguro = False
        self.lista_productos.append(producto)

        if seguro:
            self.costo_total += producto.precio * 0.15
        else:
            self.costo_total += producto.precio