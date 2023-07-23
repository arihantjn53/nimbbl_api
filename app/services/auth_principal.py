from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta

from jose import JWTError, jwt
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from app.daos import user
from app.db import get_session
from app.models.user import User as UserModel
from app.schemas.token import Token, TokenData
from app.schemas.user import ChangePasswordIn, UserIn, UserOut
from app.services.utils import UtilsService, oauth2_scheme
from app.settings import settings
from app.schemas.token import TokenIn

class AuthPrincipalService:
    
    @staticmethod
    async def generate_token(token_data: TokenIn, session: AsyncSession):
        