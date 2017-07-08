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

    def buscar(self,palabra):
        self.c.execute("SELECT * FROM cuentaCorreo WHERE direccion LIKE ?",("%"+palabra+"%",))
        lista = []

        for e in self.c:
            cuenta = {"id": e[0],"nombre": e[1],"direccion":e[2],"contraseña":e[3]}
            lista.append(cuenta)

        return lista
