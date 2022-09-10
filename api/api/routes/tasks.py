from fastapi import APIRouter, Header, Body, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# Python
from typing import List, Union
# Model
from api.models import Todo
# DB
from api.db import db
# Utils
from api.utils import get_authorization_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/", response_model=List[Todo])
async def get_todos(Authorization: str = Header(default=None)):
    user = await get_authorization_user(Authorization)
    cursor = db.todos.find({"user_id": user["username"]})
    return list(await cursor.to_list(length=100))


@router.post(
    '/create',
    status_code=status.HTTP_201_CREATED
)
async def create_todo(todo: Todo = Body(...), Authorization: str = Header(default=None)):
    user = await get_authorization_user(Authorization)
    print(user)
    todo.user_id = user["username"]
    created_task = await db.todos.insert_one(todo.dict())
    return str(created_task.inserted_id)
