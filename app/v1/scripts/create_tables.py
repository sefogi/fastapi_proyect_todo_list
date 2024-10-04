from app.v1.model.user_model import User
from app.v1.model.todo_model import Todo

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([User, Todo])
        
#En este archivo importamos los modelos User y Todo además del objeto de la base de datos y después definimos una función que se conectará a la base de datos, recibirá una lista de los modelos que queremos convertir en tablas y después cerrará la conexión.

#Para ejecutar este script, en la terminal vamos al directorio raíz de nuestro proyecto y escribimos py o python para acceder a la terminal de Python y poder ejecutar código en este lenguaje.