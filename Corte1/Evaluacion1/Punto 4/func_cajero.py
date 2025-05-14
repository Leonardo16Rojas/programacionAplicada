

class Cajero:
    def __init__(self, saldo_inicial=0):#Saldo inicial 
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        print(f"\nTu saldo actual es: ${self.saldo:.2f}")

    def depositar(self):
        try:
            monto = float(input("Ingrese el monto a depositar: "))
            if monto <= 0:
                print("Error: El monto debe ser mayor a cero.")
            else:
                self.saldo += monto
                print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
        except ValueError: 
            print("Error: Entrada inválida. Debe ingresar un número.")

    def retirar(self):
        try:
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= 0:
                print("Error: El monto debe ser mayor a cero.")
            elif monto > self.saldo:
                print("Error: Fondos insuficientes.")
            else:
                self.saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número.")
