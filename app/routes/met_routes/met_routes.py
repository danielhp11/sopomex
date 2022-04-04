from models.models import Usuario
class Validado:

    def validarRegistro(usuario,correo,clave1,clave2):
        usu_valid = {
            'usuario':'',
            'correo':'',
            'clave':'',
        }
        existe_usuario = Usuario.query.filter_by(usuario=usuario).first()

        if not usuario :
            usu_valid['respuesta']='El campo del usuario se encuentra vació'
            usu_valid['estado'] = 400
        elif existe_usuario:
            usu_valid['respuesta'] = 'La dirección de correo electrónico que ha ingresado ya está registrada'
            usu_valid['estado'] = 400
        elif not correo:
            usu_valid['respuesta']='El campo del correo se encuentra vació'
            usu_valid['estado'] = 400
        elif not clave1 or not  clave2:
            usu_valid['respuesta']= 'El campo de la contraseña se encuentra vació'
            usu_valid['estado'] = 400
        elif clave1 != clave2:
            usu_valid['respuesta']= 'Las contraseñas ingresadas deben ser idénticas'
            usu_valid['estado'] = 400
        else:
            usu_valid['usuario'] = usuario
            usu_valid['correo'] = correo
            usu_valid['clave'] = clave1

        return usu_valid