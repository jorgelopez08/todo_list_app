from fastapi import FastAPI
#Routers
from api.routes.auth import router as auth

app = FastAPI()

app.include_router(
    auth, 
    prefix='/auth',
    tags=['Authentication']
)

@app.get('/')
def index():
    return "Hello, world!"

