from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#Routers
from api.routes.auth import router as auth
from api.routes.tasks import router as task
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    auth, 
    prefix='/auth',
    tags=['Authentication']
)

app.include_router(
    task, 
    prefix='/todos',
    tags=['Todos']
)

@app.get('/')
def index():
    return "Hello, world!"

