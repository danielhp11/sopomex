from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models.models import Usuario,Colonia,Estado,Municipio,Zona
from database import db
from schema.schemas import usuario_schema,colonia_schema,colonias_schema,estado_schema,estados_schema,municipio_schema,municipios_schema,zona_schema,zonas_schema 
import bcrypt
import xlrd


blue_print = Blueprint('app', __name__)

# Ruta  inicio
@blue_print.route('/', methods=['GET'])
def inicio():
    municipios = insertMunicipio()
    colonias = insertColonias()
    zonas = insertZonas()
    insertEstado(municipios,colonias,zonas)
    try:
        estados = Estado.query.all()
        respuesta = estados_schema.dump(estados)
        return estados_schema.jsonify(respuesta), 200
    except Exception:
        return jsonify(respuesta='Error en Petición'), 500
    return jsonify(respuesta='Bienvenido a SOPOMEX',municipio = municipios,colonia = colonias,zona=zonas)


# Ruta de Registro de Usuario
@blue_print.route('/auth/registrar', methods=['POST'])
def registrar_usuario():
    try:
        # obtener el usuario
        usuario = request.json.get('usuario')
        # obtener la clave
        correo = request.json.get('correo')
        # obtener la clave
        clave1 = request.json.get('clave1')
        clave2 = request.json.get('clave2')

        if not usuario or not correo or not clave1 or not clave2:
            return jsonify(respuesta='Campos Invalidos'), 400
        
        #comprobar si el usuario existe
        existe_usuario = Usuario.query.filter_by(correo=correo).first() 
        if existe_usuario:
            return jsonify(respuesta='Usuario Ya Existe'), 400
        
                # Encriptamos clave de usuario
        clave_encriptada = bcrypt.hashpw(
            clave1.encode('utf-8'), bcrypt.gensalt())

        # Creamos el Modelo a guardar en DB
        nuevo_usuario = Usuario(usuario, correo ,clave_encriptada)

        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify(respuesta='Usuario Creado Exitosamente'), 201
        
    except Exception as e:
        return jsonify(respuesta='Error en Petición'+str(e)), 500


# Ruta para Iniciar Sesion
@blue_print.route('/auth/login', methods=['POST'])
def iniciar_sesion():
    try:
        # obtener el usuario
        correo = request.json.get('correo')
        # obtener la clave
        clave = request.json.get('clave')

        if not correo:
            return jsonify(respuesta='El campo del correo se encuentra vació'), 400
        if not clave:
            return jsonify(respuesta='El campo de la contraseña se encuentra vació'), 400
        # Consultar la DB
        existe_usuario = Usuario.query.filter_by(correo=correo).first()

        if not existe_usuario:
            return jsonify(respuesta='El correo ingresado no existe'), 404

        es_clave_valida = bcrypt.checkpw(clave.encode(
            'utf-8'), existe_usuario.clave.encode('utf-8'))

        # Validamos que sean iguales las claves
        if es_clave_valida:
            access_token = create_access_token(identity=correo)
            return jsonify(access_token=access_token), 200
    except Exception:
        return jsonify(respuesta='Error en Petición'), 500

# Ruta - Obtener estados
@blue_print.route('/auth/estados', methods=['GET'])
def obtener_estados():
    try:
        estados = Estado.query.all()
        respuesta = estados_schema.dump(estados)
        return estados_schema.jsonify(respuesta), 200
    except Exception:
        return jsonify(respuesta='Error en Petición'), 500

##########RUTAS PROTEGITAS POR JWT##########

# Ruta - Obtener municipio
@blue_print.route('/api/municipio', methods=['GET'])
@jwt_required()
def obtener_municipios():
    try:
        municipios = Municipio.query.all()
        respuesta = municipios_schema.dump(municipios)
        return municipios_schema.jsonify(respuesta), 200
    except Exception:
        return jsonify(respuesta='Error en Petición'), 500

##################METODOS PARA EXTRAR DATOS DEL ARCHIVO EXCEL########
archivo = "routes/CPdescarga.xls"
wb = xlrd.open_workbook(archivo)
def insertMunicipio():
    municipios =[]
    index = 0
    for item in wb.sheet_names():
        #print(item)
        hoja = wb.sheet_by_index(index)
        for y in range(1,hoja.nrows):
            #dos estados al iniciar el arreglo vacio o lleno
            #Si esta vacio se inserta el primer valor
            #Si esta lleno se debe recorrer el arreglo e insertar el que sea diferente a los del arreglo
            if not hoja.cell_value(y,3) in municipios:
                municipios.append(hoja.cell_value(y,3))
                nuevo_municipio = Municipio(hoja.cell_value(y,3))
                db.session.add(nuevo_municipio)   
                db.session.commit() 
        index+=1
    return municipios
    
def insertColonias():
    colonias =[]
    index = 0
    #print("Las colonias son")
    for item in wb.sheet_names():
        hoja = wb.sheet_by_index(index)
        for y in range(1,hoja.nrows):
            #dos estados al iniciar el arreglo vacio o lleno
            #Si esta vacio se inserta el primer valor
            #Si esta lleno se debe recorrer el arreglo e insertar el que sea diferente a los del arreglo
            if not hoja.cell_value(y,2) in colonias:
                colonias.append(hoja.cell_value(y,2))
                nueva_colonia = Colonia(hoja.cell_value(y,2))
                db.session.add(nueva_colonia)   
                db.session.commit() 
        index+=1
    return colonias

def insertZonas():
    zonas =[]
    index = 0
    for item in wb.sheet_names():
        hoja = wb.sheet_by_index(index)
        for y in range(1,hoja.nrows):
            #dos estados al iniciar el arreglo vacio o lleno
            #Si esta vacio se inserta el primer valor
            #Si esta lleno se debe recorrer el arreglo e insertar el que sea diferente a los del arreglo
            if not hoja.cell_value(y,13) in zonas:
                zonas.append(hoja.cell_value(y,13))
                nueva_zona = Zona(hoja.cell_value(y,13))
                db.session.add(nueva_zona)   
                db.session.commit()
        index+=1
    return zonas

def insertEstado(mun,col,zon):
    index = 0
    #Recorrer las hojas
    for item in wb.sheet_names():
        #cargar los datos de la hoja
        hoja = wb.sheet_by_index(index)
        #recorremos las filas
        for fila in range(1,hoja.nrows):
            nuevo_estado = Estado(hoja.cell_value(fila,0),hoja.cell_value(fila,1),
            str(col.index(hoja.cell_value(fila,2))+1),
            str(mun.index(hoja.cell_value(fila,3))+1),
            hoja.cell_value(fila,4),hoja.cell_value(fila,5),
            hoja.cell_value(fila,6),hoja.cell_value(fila,7),hoja.cell_value(fila,8),hoja.cell_value(fila,9),hoja.cell_value(fila,10),
            hoja.cell_value(fila,11),hoja.cell_value(fila,12),
            str(zon.index(hoja.cell_value(fila,13))+1),
            hoja.cell_value(fila,14))
            db.session.add(nuevo_estado)   
            db.session.commit()
        index+=1
    
###############FIN DE LOS METODOS DE EXCEL#################