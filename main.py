import os
from Auto import Auto
from Cliente import Cliente
from Compra import Compra

carros = []
clientes = []

def registrar_Carros():
    placa = input("Ingrese la placa del Auto: ")
    marca = input("Ingrese la marca del Auto: ")
    modelo = input("Ingrese el modelo del Auto: ")
    descripcion = input("Ingrese la descripcion del Auto: ")
    precio_unitario = input("Ingrese el precio del Auto: Q")

    carro_nuevo = Auto(placa, marca, modelo, descripcion, precio_unitario)
    carros.append(carro_nuevo)
    print(f"Carro agregado correctamente.")

def registrar_Cliente():
    nombre = input("Ingrese el nombre del Cliente: ")
    correo = input("Ingrese el correo del Cliente: ")
    nit = input("Ingrese el NIT del Cliente: ")

    cliente_nuevo = Cliente(nombre,correo,nit)
    clientes.append(cliente_nuevo)
    print(f"El Cliente {nombre} se registro correctamente.")

def realizar_Compra():
    print(clientes)
    nit_cliente = input("Ingrese el numero de NIT del Cliente: ")
    cliente = None

    for buscando_nit in clientes:
        if buscando_nit.nit == nit_cliente:
            cliente == buscando_nit

        if not cliente:
            print("NIT de Cliente no encontrado")
        
    compra_nueva = Compra(cliente)
    while True:
        print("-----MENU DE COMPRA-----")
        print("1. Agregar Auto")
        print("2. Terminar compra y generar factura")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("\nPor favor ingrese un caracter válido...")
            continue
        if opcion == 1:
            print("Agregar auto")
        
        elif opcion == 2:
            print("Terminar Compra y Generar Factura")
            break
        
        else:
            print("Igrese una opcion válida")
        input("\n Presione una tecla para continuar")



def limpiar_consola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

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
            print("\nregistro de auto")
            registrar_Carros()
        
        elif opcion == 2:
            #print("\nregistro de cliente")
            registrar_Cliente()
        
        elif opcion == 3:
            print("\nrealizo compra")
            realizar_Compra()
        
        elif opcion == 4:
            print("\nreporte de compras")
        
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
