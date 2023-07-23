from datetime import datetime, timedelta

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.daos import auth_principal, order
from app.schemas.token import Token, TokenIn
from app.services.utils import UtilsService
from app.settings import settings


class GenerateTokenService:
    @staticmethod
    async def generate_token(token_data: TokenIn, session: AsyncSession):
        _auth_principal = await auth_principal.AuthPrincipalDao(session).get_by_key_secret(token_data)

        if not _auth_principal:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect access key or secret.",
            )

        if token_data.order_id:
            _order = await order.OrderDao(session).get_by_order_id(token_data.order_id)
            sub_merchant_id = _order.sub_merchant_id
        else:
            sub_merchant_id = _auth_principal.sub_merchant_id

        access_token_expires = timedelta(seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = UtilsService.create_access_token(
            data={
                "user_id": _auth_principal.id,
                "sub_merchant_id": sub_merchant_id,
                "type": _auth_principal.type,
                "token_type": "transaction",
            },
            expires_delta=access_token_expires,
        )

        token_data = {
            "token": access_token,
            "token_type": "Bearer",
            "expires_at": datetime.now() + access_token_expires,
            "sub_merchant_id": sub_merchant_id,
            "auth_principal": {
                "sub_merchant_id": sub_merchant_id
            }
        }
        return Token(**token_data)
