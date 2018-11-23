from flask import Flask 
from flask import url_for, jsonify, render_template, request
from logica import *

app = Flask(__name__)

saborInput = 1
porcionInput = 1


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/checar')
def checar():
    print("sabor input:", saborInput)
    print("porcion input:", porcionInput)
    return "nothing"

@app.route('/calcular')
def calcular():
    if saborInput == 1 or porcionInput == 1:
        error = ("Ingrese un sabor y una porcion e intente de nuevo")
        return jsonify({'precio': error})
    else:
        precio = logica(saborInput, porcionInput)
        precioFinal = (precio, " pesos")
        return jsonify({'precio': precioFinal})

@app.route('/saborDulce')
def saborDulce():
    global saborInput
    saborInput = 0
    print("Sabor dulce es:", saborInput)
    saborDulce = ("Dulce")
    return jsonify({'sabor': saborDulce})

@app.route('/saborAgridulce')
def saborAgridulce():
    global saborInput
    saborInput = 25
    print("Sabor Agridulce es:", saborInput)
    saborAgridulce = ("Agridulce")
    return jsonify({'sabor': saborAgridulce})

@app.route('/saborPicante')
def saborPicante():
    global saborInput
    saborInput = 55
    print("Sabor Picante es:", saborInput)
    saborPicante = ("Picante")
    return jsonify({'sabor': saborPicante})

@app.route('/saborSalado')
def saborSalado():
    global saborInput
    saborInput = 90
    print("Sabor Salado es:", saborInput)
    saborSalado = ("Salado")
    return jsonify({'sabor': saborSalado})

@app.route('/porcionChica')
def porcionChica():
    global porcionInput
    porcionInput = 0
    print("Porcion chica es:", porcionInput)
    porcionChica = ("Chica")
    return jsonify({'porcion': porcionChica})

@app.route('/porcionMediana')
def porcionMediana():
    global porcionInput
    porcionInput = 40
    print("Porcion mediana es:", porcionInput)
    porcionMediana = ("Mediana")
    return jsonify({'porcion': porcionMediana})

@app.route('/porcionGrande')
def porcionGrande():
    global porcionInput
    porcionInput = 87
    print("Porcion grande es:", porcionInput)
    porcionGrande = ("Grande")
    return jsonify({'porcion': porcionGrande})
    
if __name__ == '__main__':
	app.run(debug=True)
