from correo import Correo

class Menu:
    c = Correo()
    def __init__ (self):
        while True:
            print("1) Mostrar usuario")
            print("2) Agregar usuario")
            print("0) Salir")
            op = input()

            if op == "1":
                self.mostrar()
            elif op == "2":
                self.agregar()
            elif op == "0":
                break

    def mostrar (self):
        filas = self.c.mostrarCuenta()
        for fila in filas:
            print("{0:2}{1:10}{2:20}{3:12}".format(fila[0],fila[1],fila[2],fila[3]))

    def agregar(self):
        nombre = input("Nombre: ")
        direccion = input("Direccion: ")
        password = input("Contraseña: ")
        self.c.insertarCuenta([nombre,direccion,password])
