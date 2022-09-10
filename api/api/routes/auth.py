"""Authentication"""
from os import stat
from fastapi import APIRouter, Body, Form, status, HTTPException
from fastapi.responses import RedirectResponse
from passlib.hash import pbkdf2_sha256 as psswd_hash
# Models
from api.models import User
# DB
from api.db import db
# JWT
import jwt


router = APIRouter()


@router.post('/login', status_code=status.HTTP_200_OK)
async def login(username: str = Form(...), password: str = Form(...)):
    user = await db.users.find_one({"username": username})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not psswd_hash.verify(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Password is incorrect")
    return jwt.encode({
        "username": user["username"],
        "password": user["password"],
    }, "secret", algorithm="HS256")
    # return RedirectResponse(url="/auth/test", status_code=status.HTTP_303_SEE_OTHER)


@router.post(
    '/register',
    status_code=status.HTTP_201_CREATED,
    response_model=User
)
async def register(user: User = Body(...)):
    user.password = psswd_hash.hash(user.password)
    new_user = await db.users.insert_one(user.dict())
    print(new_user.inserted_id)
    return user


@router.get('/test')
async def test():
    return "test"
