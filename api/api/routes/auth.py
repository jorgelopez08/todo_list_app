"""Authentication"""
from fastapi import APIRouter, Body, Form, status
from passlib.hash import pbkdf2_sha256 as psswd_hash
# Models
from api.models import User
# DB
from api.db import db


router = APIRouter()


@router.post('/login')
async def login():
    pass


@router.post(
    '/register',
    status_code=status.HTTP_201_CREATED,
    response_model=User
)
async def register(user: User = Body(Ellipsis)):
    user.password = psswd_hash.hash(user.password)
    new_user = await db.users.insert_one(user.dict())
    print(new_user.inserted_id)
    return user
