"""
5 - Crea una clase cuenta bancaria. Los atributos iniciales son “titular” y “saldo”.
El saldo inicial es 0. La clase debe tener dos métodos, ingresar y retirar. Cuando
creas un objeto cliente, debe tener los parámetros nombre y saldo. En función de eso, un
objeto puede ejecutar el método ingresar o retirar, pero si intenta
retirar un valor más alto que el saldo, debe salir un mensaje de saldo insuficiente.
"""
class Cuenta_bancaria():
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self):
        print(f"Hola {self.titular}")
        print(f"Saldo actual {self.saldo}")
        a = int(input("Cuanto desea ingresar?\n"))
        self.saldo += a
        print(f"Nuevo saldo: {self.saldo}")

    def retirar(self):
        print(f"Hola {self.titular}")
        print(f"Saldo actual {self.saldo}")
        b = int(input("Cuanto desea retirar?\n"))
        if b > self.saldo:
            print("Error Saldo insuficiente")
        else:
            self.saldo -= b
            print(f"Nuevo saldo: {self.saldo}")



cliente = Cuenta_bancaria("Marcos",500)

cliente.ingresar()
cliente.retirar()