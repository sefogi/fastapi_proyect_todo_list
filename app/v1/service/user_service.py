from fastapi import HTTPException, status

from passlib.context import CryptContext

from app.v1.model.user_model import User as UserModel
from app.v1.schema import user_schema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(user: user_schema.UserRegister):

    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.username == user.username)).first()
    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )

    db_user.save()

    return user_schema.User(
        id = db_user.id,
        username = db_user.username,
        email = db_user.email
    )
'''
En este archivo primero importamos HTTPException y status de FastAPI. La primera la usaremos cuando queramos lanzar una excepción controlada por FastAPI. Si lanzamos esta excepción, podremos customizar una respuesta para el usuario en formato JSON y con un código de estado de HTTP.

Status de FastAPI contiene los códigos de estado HTTP almacenados en constantes en el que en los nombres de las constantes tendremos información del significado del código de estado. Esto lo utilizaremos cuando queramos lanzar una excepción de tipo HTTPException.

Después importamos CryptContext que será la librería que emplearemos para encriptar las contraseñas.

Por último importamos nuestro modelo de usuario de peewee para poder crear el usuario y el modelo de usuario de Pydantic para retornar al usuario la información del usuario creado.

Ahora que hemos explicado los imports vamos con la siguiente parte del código. Primero creamos una instancia de CryptContext y posteriormente definimos una función llamada get_password_hash que encriptará la contraseña utilizando la instancia de CryptContext que acabamos de crear.

La siguiente función se llama create_user y recibe un modelo de Pydantic de tipo UserRegister. Esta función se encargará de guardar el usuario en la base de datos. Comprobamos si el usuario enviado ya existe en la base de datos por email o por username, si es así, lanzaremos una excepción HTTPException con el código de estado 400 y en el detail explicaremos el porqué del error.

Después usando el modelo de usuario de peewee, creamos el usuario con la contraseña encriptada y lo guardamos.

Por último retornamos la información del usuario recién creado empleando el modelo User de Pydantic.
'''