
def mostrar_menu():
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("Seleccione una opción (Ctrl + Z para salir): ", end='')

def ejecutar_menu(cajero):
    while True:
        try:
            mostrar_menu()
            opcion = input()
            if opcion == '1':
                cajero.consultar_saldo()
            elif opcion == '2':
                cajero.depositar()
            elif opcion == '3':
                cajero.retirar()
            else:
                print("Opción inválida. Intente de nuevo.")
        except EOFError:
            print("\nSaliendo del cajero. ¡Gracias por usar el servicio!")
            break

