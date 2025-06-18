from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


@app.route("/guardar", methods=["POST"])
def guardar():
    Nombre = request.form.get("Nombre")
    Correo = request.form.get("Correo")
    Mensaje = request.form.get("Mensaje")
    return render_template("guardar.html", Nombre=Nombre, Correo=Correo, Mensaje=Mensaje)

if __name__ == "__main__":
    app.run(debug=True)