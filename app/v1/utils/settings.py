import os #con esta libreria podemos leer las variables de entorno

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()
#clase BaseSettings y la función load_dotenv de la librería python-dotenv la cual se encargará de leer las variables de entorno.

#Después declaramos la clase Settings que extenderá de BaseSettings y para finalizar declaramos las variables que guardarán la información sobre la conexión y autenticación a la base de datos.
class Settings(BaseSettings):
    # Add your environment variables here
    
    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')
    
    secret_key: str = os.getenv('SECRET_KEY')
    token_expire: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES') 
    
#Los valores los asignamos gracias a la función getenv de la librería os la cual recibe el nombre que les dimos a las variables de entorno en el archivo .env y si existen retornan su valor. Si no es así, devolverá None.

"""
Una vez añadidas las nuevas variables de entorno al proyecto es hora de ponernos manos a la obra con la autenticación. Para ello, primero vamos a instalar librería que usaremos para trabajar con JWT así que lanzamos el siguiente comando para instalarla:

pip install "python-jose[cryptography]"

También necesitaremos instalar python-multipart. Para ello lanzamos el siguiente comando:

pip install python-multipart


"""