import peewee

from app.v1.utils.db import db

#Esta clase extiende de peewee.Model y en ella declaramos los campos que vamos a necesitar que será un email, username y password. El id no es necesario definirlo, ya que peewee se encargará de crearlo automáticamente como clave primaria y autoincrement.
class User(peewee.Model):
    email= peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()
    
#Después añadimos la clase Meta dentro de la clase User que contendrá la conexión a la base de datos.    
    class Meta:
        database = db
        
# más información acerca de que tipos de datos podéis crear con peewe
# https://docs.peewee-orm.com/en/latest/
    