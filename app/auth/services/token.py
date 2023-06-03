from datetime import datetime, timedelta

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from starlette import status

from app.api.config.base import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_access_token(user_id: int, email: str):
    now = datetime.utcnow()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expires = now + expires_delta
    to_encode = {"user_id": user_id, "email": email, "exp": expires}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        email = payload.get("email")
        return User(id=user_id, email=email)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

async def validate_token(token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    return user
