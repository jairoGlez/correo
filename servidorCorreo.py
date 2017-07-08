from flask import Flask, jsonify, request
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
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return(respuesta)

@app.route("/nuevaCuenta", methods=["POST"])
def nuevaCuenta():
    print(request.form)
    nombre = request.form["nombre"]
    direccion = request.form["direccion"]
    password = request.form["password"]
    cuenta.insertarCuenta([nombre,direccion,password])

    respuesta = jsonify({"status":"Ok"})
    respuesta.headers.add("Access-Control-Allow-Origin","*")
    return respuesta

app.run()
