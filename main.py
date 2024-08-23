import os
from Auto import Auto
from Cliente import Cliente

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
    pass


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
