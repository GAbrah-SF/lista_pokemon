from flask import Flask, render_template
from titulos import title1, titulo1
from formularios import ver_formularios
from lista_clientes import ver_clientes
from lista_productos import ver_productos
from lista_ventas import ver_ventas
from lista_databases import mostrar_DataBase

app = Flask(__name__)

verdad = True
puerto = 2210


@app.route('/')
def home():
    return render_template("index.html", title1=title1, titulo1=titulo1)


@app.route('/Formularios')
def formularios():
    return ver_formularios()


@app.route('/Clientes')
def clientes():
    return ver_clientes()


@app.route('/Productos')
def productos():
    return ver_productos()


@app.route('/Ventas')
def ventas():
    return ver_ventas()


@app.route('/DataBases')
def DataBases():
    return mostrar_DataBase()


if __name__ == '__main__':
    app.run(debug=verdad, port=puerto)
