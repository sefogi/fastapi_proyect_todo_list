from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username:Optional[str] = None
    

""""
En este caso tendremos la clase Token que será el objeto que usaremos para retornarle el token de autenticación y el tipo de autenticación y luego tendremos una clase TokenData que almacenará el nombre de usuario en el token. Aquí podríamos guardar más información que nos podría ser útil en el token y cuando lo decodificásemos poder utilizarla.

Como podéis observar, aquí empleamos un tipo nuevo llamado Optional que recibe el tipo de dato e indica que ese campo será opcional. En este caso no estamos usando Field y por defecto le daremos un valor de None.


Nuevas variables de entorno
Ahora que ya tenemos nuestro modelo para los tokens, el siguiente paso será crear un para de variables de entorno llamadas ACCESS_TOKEN_EXPIRE_MINUTES y SECRET_KEY. La primera contendrá el tiempo de validez máximo de un token en minutos y la segunda una clave para codificar y decodificar nuestros tokens

"""