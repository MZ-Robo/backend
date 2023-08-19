import jwt
from datetime import datetime, timedelta
from typing import Optional, Union
from pydantic import BaseModel

# Configuration constants
# Example key, change it for production and store it securely.
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class TokenData(BaseModel):
    username: str


def create_access_token(data: dict) -> str:
    """
    Generate a new access token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Union[TokenData, None]:
    """
    Decode an access token and retrieve user information.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_data = TokenData(username=payload.get("sub"))
        return user_data
    except jwt.JWTError:
        return None


def verify_access_token(token: str) -> bool:
    """
    Verify the validity of an access token.
    """
    decoded_data = decode_access_token(token)
    if not decoded_data:
        return False
    # Additional verification can be added here.
    return True
