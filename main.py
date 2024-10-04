from fastapi import FastAPI
from app.v1.router.user_router import router as user_router

app = FastAPI()


app.include_router(user_router)

"""
El primer cambio que podéis ver es que hemos importado el router que acabamos de crear. Luego de instanciar FastAPI incluimos el router de usuario dentro de la app gracias al método include_router. Esto nos permitirá añadir rutas a nuestro proyecto desde otros archivos (como user_router).

Por último, he eliminado el endpoint que creamos de ejemplo, ya que no lo necesitaremos.
"""