#Se importan las clases de los otros archivos para utilizar los objetos y sus atributos
import os
from Auto import Auto
from Cliente import Cliente
from Compra import Compra

#Se crean las listas que contienen los datos ingresados
carros = []
clientes = []
compras =[]

#En este metodo se registran todos los carros que se ingresan por el usuario, se agregan a la lista carros
def registrar_Carros():
    placa = input("\nIngrese la placa del Auto: ")
    marca = input("Ingrese la marca del Auto: ")
    modelo = input("Ingrese el modelo del Auto: ")
    descripcion = input("Ingrese la descripcion del Auto: ")
    precio_unitario = float(input("Ingrese el precio del Auto: Q"))

    carro_nuevo = Auto(placa, marca, modelo, descripcion, precio_unitario)
    carros.append(carro_nuevo)
    print(f"\nCarro agregado correctamente.")

#Esta funcion sirve para recorrer la lista de los carros ingresados y mostrarlos en consola
def mostrar_carros_registrados(carros):
    print("\n----------Lista de Autos Disponibles-----------")
    for carro in carros:
        print(f"Placa: {carro.placa}, Marca: {carro.marca}, Modelo: {carro.modelo}, Precio: Q{carro.precio_unitario: .2f}")

#En este metodo se registran todos los clientes que se ingresan por el usuario, se agregan a la lista clientes
def registrar_Cliente():
    nombre = input("\nIngrese el nombre del Cliente: ")
    correo = input("Ingrese el correo del Cliente: ")
    nit = input("Ingrese el NIT del Cliente: ")

    cliente_nuevo = Cliente(nombre,correo,nit)
    clientes.append(cliente_nuevo)
    print(f"\nEl Cliente {nombre} se registro correctamente.")

#Esta funcion sirve para recorrer la lista de los clientes ingresados y mostrarlos en consola
def mostrar_clientes_registrados(clientes):
    print("\n-----------Lista de Clientes Registrados---------- ")
    for cliente in clientes:
        print(f"Nombre: {cliente.nombre}, NIT: {cliente.nit}, Correo: {cliente.correo}")

#Aqui se crea el reporte general de compras, que lista todas las facturas creadas por loas compras realizadas
def reporte_compras():
    print("\n=========================REPORTE DE COMPRAS=====================================")
    #Aqui se recorre la lista que contiene las facturas de las compras y las va imprimiendo en consola
    for compra in compras:
        compra.generar_factura()
    total_general = 0.0

    #Aqui calculamos el total de la suma de las facturas creadas 
    for compra in compras:
        total_general += compra.costo_total
    print("------------------------------------------------------------------------------------")
    print(f"Total General de Compras: Q{total_general:.2f}")


def realizar_Compra():
    ##Muestra el listado de cllientes registrados
    mostrar_clientes_registrados(clientes)
    nit_cliente = input("\nIngrese el numero de NIT del Cliente: ")
    cliente = None

    #Hace la validacion para saber si el nit ingresado existe o no
    for buscando_nit in clientes:
        if buscando_nit.nit == nit_cliente:
            cliente = buscando_nit
    if not cliente:
        print("NIT de Cliente no encontrado")
        return 
    compra_nueva = Compra(cliente)
    #print(compra_nueva)

    #Se crea el sub menu que sirve para gestionar la compra
    while True:

        print("\n--------MENU DE COMPRA---------")
        print("1. Agregar Auto")
        print("2. Terminar compra y generar factura")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("\nPor favor ingrese un caracter válido...")
            continue

        if opcion == 1:
            #print("Agregar auto")
            #Muestra el listado de carros registrados
            mostrar_carros_registrados(carros)

            placa_carro_comprado = input("\nIngrese la Placa del Auto que desea comprar...")
            carro_comprado = None
            #Recorre la lista de carros y valida que la placa ingresada exista
            for auto in carros:
                if auto.placa == placa_carro_comprado:
                    carro_comprado = auto
            
            if not carro_comprado:
                print("Placa del Auto no encontrada")
                return
            #Aqui se valida la opcion de agregar el seguro al costo del carro
            else:
                seguro = input("\n¿Desea agregar seguro? (SI/NO): ").strip().upper() == "SI"
                compra_nueva.agregar_producto(carro_comprado, seguro)


        #En esta opcion se muestran las facturas generadas por cada compra del cliente y se da por finalizada la compra
        elif opcion == 2:
            compra_nueva.generar_factura()
            compras.append(compra_nueva)
            print("\n Factura de Compra Generada EXitosamente")
            break
            
        else:
            print("Igrese una opcion válida")
        input("\n Presione una tecla para continuar")

#Sirve para limpiar la consola 
def limpiar_consola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Menu principal que contine todos los metodos del programa
def Menu():
    while True:
       
        print("\n //////-SUPER AUTOS GT-/////\n")
        print("1. Registrar Auto")
        print("2. Registrar Cliente")
        print("3. Realizar Compra")
        print("4. Reporte de Compras")
        print("5. Datos del Estudiante")
        print("6. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opcion para continuar... "))
        except ValueError:
            print("\n Por favor ingrese un caracter valido")
            continue
             
        if opcion == 1:
            #print("\nregistro de auto")
            registrar_Carros()
        
        elif opcion == 2:
            #print("\nregistro de cliente")
            registrar_Cliente()
        
        elif opcion == 3:
            #print("\n Compra Realizada EXitosamente")
            realizar_Compra()
        
        elif opcion == 4:
            #print("\nreporte de compras")
            reporte_compras()
        elif opcion == 5:
            print("\n---Datos del Estudiante---")
            print("-Leonel Antonio Gonzalez Garcia")
            print("-201709088")
        
        elif opcion == 6:
            print("\n Gracias por su Compra, vuelva pronto :) \n")
            break
        else:
            print("\nPor favor seleccione una opcion valida")
        input("\nPresione cualquier tecla para continuar...")
        limpiar_consola()


if __name__ == "__main__":
    Menu()
