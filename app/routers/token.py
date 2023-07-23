from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.schemas.token import TokenIn
from app.services.generate_token import GenerateTokenService

router = APIRouter(tags=["Token"])

@router.post("/generate-token", status_code=status.HTTP_200_OK)
async def generate_token(
    token_data: TokenIn,
    session: AsyncSession = Depends(get_session),
):
    return await GenerateTokenService.generate_token(token_data, session)
