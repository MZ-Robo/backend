from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from domain.user import user_schema
from token_utils import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> user_schema.TokenData:
    user_data = decode_access_token(token)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user_data
