from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.daos.base import BaseDao
from app.models.auth_principal import AuthPrincipal
from app.schemas.token import TokenIn


class AuthPrincipalDao(BaseDao):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def create(self, auth_principal_data) -> AuthPrincipal:
        _auth_principal = AuthPrincipal(**auth_principal_data)
        self.session.add(_auth_principal)
        await self.session.commit()
        await self.session.refresh(_auth_principal)
        return _auth_principal

    async def get_by_id(self, auth_principal_id: int) -> AuthPrincipal | None:
        statement = select(AuthPrincipal).where(AuthPrincipal.id == auth_principal_id)
        return await self.session.scalar(statement=statement)

    async def get_by_key_secret(self, token_data: TokenIn) -> AuthPrincipal | None:
        statement = select(AuthPrincipal).where(AuthPrincipal.access_key == token_data.access_key, AuthPrincipal.access_secret == token_data.access_secret)
        return await self.session.scalar(statement=statement)
    
    async def get_all(self) -> list[AuthPrincipal]:
        statement = select(AuthPrincipal).order_by(AuthPrincipal.id)
        result = await self.session.execute(statement=statement)
        return result.scalars().all()

    async def delete_all(self) -> None:
        await self.session.execute(delete(AuthPrincipal))
        await self.session.commit()

    async def delete_by_id(self, auth_principal_id: int) -> AuthPrincipal | None:
        _auth_principal = await self.get_by_id(auth_principal_id=auth_principal_id)
        statement = delete(AuthPrincipal).where(AuthPrincipal.id == auth_principal_id)
        await self.session.execute(statement=statement)
        await self.session.commit()
        return _auth_principal
