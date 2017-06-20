import sqlite3

db = sqlite3.connect("correo.db")
c = db.cursor()

def mostrarCuenta():
    r = c.execute("SELECT * FROM cuentaCorreo")
    r = r.fetchall()

    for fila in r:
        print(fila)

def insertarCuenta(datos):
    c.execute("INSERT INTO  cuentaCorreo (nombre, direccion, contraseña) VALUES (?,?,?)",
    (datos[0],datos[1],datos[2]))
    db.commit()

insertarCuenta(["luis","luis877@gmail.com","contraseña"])
mostrarCuenta()
