from database import db

#Clase mapeada a la tabla Usuario en la base de datos
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(70), nullable=False)
    correo = db.Column(db.String(70), nullable=False, unique=True)
    clave = db.Column(db.String(100), nullable=False)

    def __init__(self, usuario,correo ,clave):
        self.usuario = usuario
        self.clave = clave
        self.correo = correo

#Clase mapeada a la tabla Estado en la base de datos
class Estado(db.Model):
    __tablename__ = 'estados'
    id = db.Column(db.Integer, primary_key=True)
    d_codigo = db.Column(db.String(5))
    d_asenta = db.Column(db.String(200))
    id_coloniafk = db.Column(db.Integer)
    id_municipiofk = db.Column(db.Integer)
    d_estado = db.Column(db.String(100))
    d_ciudad = db.Column(db.String(200))
    d_cp = db.Column(db.String(5))
    c_estado = db.Column(db.String(2))
    c_oficina = db.Column(db.String(5))
    c_cp = db.Column(db.String(100))
    c_tipo_asenta = db.Column(db.String(2))
    cmnpio = db.Column(db.String(3))
    id_asenta_cpcons = db.Column(db.String(5))
    id_zonaFK = db.Column(db.Integer)
    c_cve_ciudad = db.Column(db.String(2))

    def __init__(self,d_codigo,d_asenta,id_coloniafk,id_municipiofk,d_estado,d_ciudad,d_cp,c_estado,c_oficina,c_cp,c_tipo_asenta,cmnpio,id_asenta_cpcons,id_zonaFK,c_cve_ciudad):
        self.d_codigo=d_codigo
        self.d_asenta=d_asenta
        self.id_coloniafk=id_coloniafk
        self.id_municipiofk=id_municipiofk
        self.d_estado=d_estado
        self.d_ciudad=d_ciudad
        self.d_cp=d_cp
        self.c_estado=c_estado
        self.c_oficina=c_oficina
        self.c_cp=c_cp
        self.c_tipo_asenta=c_tipo_asenta
        self.cmnpio=cmnpio
        self.id_asenta_cpcons=id_asenta_cpcons
        self.id_zonaFK=id_zonaFK
        self.c_cve_ciudad=c_cve_ciudad    

#Clase mapeada a la tabla Usuario en la base de datos
class Municipio(db.Model):
    __tablename__ = 'municipios'
    id = db.Column(db.Integer, primary_key=True)
    municipio = db.Column(db.String(200))
    def __init__(self,municipio):
        self.municipio = municipio

class Colonia(db.Model):
    __tablename__ = 'colonias'
    id = db.Column(db.Integer, primary_key=True)
    colonia = db.Column(db.String(200))
    def __init__(self,colonia):
        self.colonia=colonia

class Zona(db.Model):
    __tablename__ = 'zonas'
    id = db.Column(db.Integer, primary_key=True)
    zona = db.Column(db.String(200))
    def __init__(self,zona):
        self.zona=zona