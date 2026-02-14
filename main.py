from modelos.tipos_cliente import *
from servicios.gestor_clientes import GestorClientes

gestor = GestorClientes()

def menu():
    while True:
        print("\n--- GIC ---")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Salir")

        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")

            tipo = input("Tipo (R/P/C): ")

            if tipo == "P":
                cliente = ClientePremium(nombre, email, telefono, direccion)
            elif tipo == "C":
                cliente = ClienteCorporativo(nombre, email, telefono, direccion)
            else:
                cliente = ClienteRegular(nombre, email, telefono, direccion)

            gestor.agregar(cliente)

        elif op == "2":
            for c in gestor.listar():
                print(c)

        elif op == "3":
            break


menu()