from flask import Flask, jsonify
from correo import Correo

app = Flask("bd")
cuenta = Correo()

@app.route("/")
def raiz():
    return("Cuenta de correo")

@app.route("/cuentas")
def cuentas():
    cuentas = cuenta.mostrarCuenta()
    print(cuentas)
    respuesta = jsonify(cuentas)
    return(respuesta)

app.run()
