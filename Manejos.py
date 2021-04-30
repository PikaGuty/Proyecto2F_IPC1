from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from Persona import Persona
from Medicamento import Medicamento
Personas = []
Medicamentos = []
app = Flask(__name__)
CORS(app)

Personas.append(Persona(1,'Javier','Gutierrez','14/03/2001',True,'PikaGuty','1234','n',42543549,1))
#Personas.append(Persona(2,'Alejandro','de León','13/03/2001',True,'Gohanale','1234','Neurólogo',42751345,1))

Medicamentos.append(Medicamento('Paracetamol',25.5,'No c sirve para todo no?',8))
Medicamentos.append(Medicamento('Tabcin',80,'Para la gripe',15))

@app.route('/Personas',methods=['GET'])
def getPersonas():
    global Personas
    Datos = []
    for i in Personas:
        objeto={
            'Id':i.getId(),
            'Nombre':i.getNombre(),
            'Apellido':i.getApellido(),
            'Fecha':i.getFechan(),
            'Sexo':i.getSexo(),
            'Nombre_us':i.getNombre_us(),
            'Contraseña ':i.getContraseña(),
            'Especialidad':i.getEspecialidad(),
            'Telefono':i.getTelefono(),
            'Tipo':i.getTipo()
        }
        Datos.append(objeto)
    return (jsonify(Datos))

@app.route('/Medicamentos',methods=['GET'])
def getMedicamentos():
    global Medicamentos
    Datos = []
    for i in Medicamentos:
        objeto={
            'Nombre':i.getNombre(),
            'Precio':i.getPrecio(),
            'Descripcion':i.getDescripcion(),
            'Cantidad':i.getCantidad()
        }
        Datos.append(objeto)
    return (jsonify(Datos))

@app.route('/Personas/<int:id>',methods=['GET'])
def OptenerPersonas(nombre):
    global Personas
    for i in Personas:
        if i.getNombre() == nombre:
            objeto={
                'Id':i.getId(),
                'Nombre':i.getNombre(),
                'Apellido':i.getApellido(),
                'Fecha':i.getFechan(),
                'Sexo':i.getSexo(),
                'Nombre_us':i.getNombre_us(),
                'Contraseña ':i.getContraseña(),
                'Especialidad':i.getEspecialidad(),
                'Telefono':i.getTelefono(),
                'Tipo':i.getTipo()
            }
            return (jsonify(objeto))
    salida = {"Mensaje":"No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Personas/<string:nombre>',methods=['GET'])
def OptenerPersonas(nombre):
    global Personas
    for i in Personas:
        if i.getNombre() == nombre:
            objeto={
                'Nombre':i.getNombre(),
                'Apellido':i.getApellido(),
                'Edad':i.getEdad()
            }
            return (jsonify(objeto))
    salida = {"Mensaje":"No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Personas',methods=['POST'])
def AgregarUsuario():
    global Personas
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    nuevo = Persona(nombre,apellido,edad)
    Personas.append(nuevo)
    return jsonify({
        'Mensaje':'Se agregó el usuario'
    })

@app.route('/Personas/<string:nombre>', methods=['PUT'])
def ActualizarPersona(nombre):
    global Personas
    for i in range(len(Personas)):
        if nombre == Personas[i].getNombre():
            Personas[i].setNombre(request.json['nombre'])
            Personas[i].setApellido(request.json['apellido'])
            Personas[i].setEdad(request.json['edad'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

@app.route('/Personas/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    global Personas
    for i in range(len(Personas)):
        if nombre == Personas[i].getNombre():
            del Personas[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)