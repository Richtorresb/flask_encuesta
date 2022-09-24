from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['nombre']
        self.last_name = data['ubicacion']
        self.email = data['idioma']
        self.email = data['comentario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM esquema_encuesta_dojo.usuarios;"
        results = connectToMySQL('esquema_encuesta_dojo').query_db(query)
        usuarios = []

        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios ( nombre , ubicacion , idioma, comentario , created_at, updated_at ) VALUES ( %(nombre)s , %(ubicacion)s , %(idioma)s, %(comentario)s , NOW() , NOW() );"

        return connectToMySQL('esquema_encuesta_dojo').query_db( query, data )
    
    
    @classmethod
    def seleccionar(cls, data ):
        query = "SELECT * FROM usuarios WHERE ( usuarios.id = %(id)s);"
        return connectToMySQL('esquema_encuesta_dojo').query_db( query, data )

    @staticmethod
    def validate(data):
        is_valid = True # asumimos que esto es true
        if len(data['nombre']) > 4:
            flash("El nombre debe tener mas de 4 caracteres.", "error")
            is_valid = False
        if len(data['ubicacion']) > 3:
            flash("La ubicacion debe tener mas de 4 caracteres.", "error")
            is_valid = False
        if len(data['idioma']) > 3:
            flash("El idioma debe ser de la seleccion", "error")
            is_valid = False
        return is_valid
    
