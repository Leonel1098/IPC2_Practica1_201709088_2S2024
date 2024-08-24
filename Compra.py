from Auto import Auto
from Cliente import Cliente


class Compra:

    #Variable contador que sirve para llevar un control de las facturas creadas
    contador_id = 1

    #Metodo constructor de la clase compra donde se crean las instancias de las variables de clientes y auto
    def __init__(self,cliente):
        self.id = Compra.contador_id
        Compra.contador_id += 1
        self.cliente = cliente
        self.lista_productos = []
        self.costo_total = 0.0

    #En esta funcion agregamos los carros a la lista junto con sus atributos
    def agregar_producto(self, producto, seguro):
        self.lista_productos.append(producto)
        precio_unitario = float(producto.precio_unitario)
        #En esta parte hacemos la validacion para calcular el percio de los carros con seguro o sin seguro
        if seguro:
            self.costo_total += precio_unitario * 0.15
        self.costo_total += precio_unitario


    #En este metodo se crea la factura de compra de cada cliente 
    def generar_factura(self):
        print("\n..................................................................")
        print(f"Factura ID: {self.id}")
        print("CLIENTE: ")
        print(f"\nNombre: {self.cliente.nombre}")
        print(f"NIT: {self.cliente.nit}")
        print(f"Correo: {self.cliente.correo}")
        print("\nLista de Carros Comprados: ")
        for carro in self.lista_productos:
            print(f"Numero de Placa: {carro.placa} - Marca: {carro.marca} -Modelo: {carro.modelo} - Precio: Q{carro.precio_unitario:.2f}")
        print(f"Total de Factura {self.id}: Q{self.costo_total:.2f}")