from dataclasses import field
from flask_marshmallow import Marshmallow

ma = Marshmallow()


# Esquema de Usuario
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usuario','correo' ,'clave')

# Esquema de Estado
class EstadoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'd_codigo','d_asenta' ,'id_coloniaFK' ,
        'id_municipioFK','d_estado','d_ciudad','d_cp','c_estado',
        'c_oficina','c_cp','c_tipo_asenta','cmnpio',
        'id_asenta_cpcons','id_zonaFK','c_cve_ciudad')
# Esquema de Municipios
class MunicipioSchema(ma.Schema):
    class Meta:
        fields =('id','municipio')
# Esquema de Colonias
class ColoniaSchema(ma.Schema):
    class Meta:
        fields=('id','colonia')
# Esquema de Zonas
class ZonaSchema(ma.Schema):
    class Meta:
        fields=('id','zona')


usuario_schema = UsuarioSchema()

estado_schema = EstadoSchema()
estados_schema = EstadoSchema(many=True)

municipio_schema  = MunicipioSchema()
municipios_schema  = MunicipioSchema(many=True)

colonia_schema = ColoniaSchema()
colonias_schema = ColoniaSchema(many=True)

zona_schema = ZonaSchema()
zonas_schema = ZonaSchema(many=True)

