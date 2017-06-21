import sqlite3

class Correo:
    db = sqlite3.connect("correo.db")
    c = db.cursor()

    def mostrarCuenta(self):
        r = self.c.execute("SELECT * FROM cuentaCorreo")
        r = r.fetchall()
        lista = []

        for fila in r:
            lista.append(fila)

        return lista

    def insertarCuenta(self,datos):
        self.c.execute("INSERT INTO  cuentaCorreo (nombre, direccion, contraseña) VALUES (?,?,?)",
        (datos[0],datos[1],datos[2]))
        self.db.commit()
