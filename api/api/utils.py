# Python
from re import A
from fastapi import HTTPException, status
# DB
from api.db import db
# Auth
import jwt


async def get_authorization_user(authorization_header):
    if not authorization_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authorization header",
        )
    authorized = jwt.decode(authorization_header, "secret", algorithms=["HS256"])
    if not authorized:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid authorization header")
    authorized_user = await db.users.find_one({"username":authorized["username"]})
    del authorized_user["_id"]
    del authorized_user["id"]
    return authorized_user