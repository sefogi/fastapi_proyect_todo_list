from datetime import datetime

import peewee

from app.v1.utils.db import db
from .user_model import User


class Todo(peewee.Model):
    title = peewee.CharField()
    create_at = peewee.DateTimeField(default=datetime.now)
    is_done = peewee.BooleanField(default=False)
    user = peewee.ForeignKeyField(User, backref="todos")
    
    class Meta:
        database = db
        
#En este caso tendremos cuatro columnas (más el id que se genera automáticamente). El campo title será una breve descripción de la tarea a realizar, created_at será la fecha de creación, un booleano llamado is_done para indicar si la tarea ya ha sido realizada o no que por defecto se guardará como false y una clave foránea user para indicar a que usuario corresponde el todo. Esto guardará en la base de datos como un campo llamado user_id.
        