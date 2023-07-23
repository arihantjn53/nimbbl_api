from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.daos.base import BaseDao
from app.models.order import Order


class OrderDao(BaseDao):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def create(self, order_data) -> Order:
        _order = Order(**order_data)
        self.session.add(_order)
        await self.session.commit()
        await self.session.refresh(_order)
        return _order

    async def get_by_id(self, order_id: int) -> Order | None:
        statement = select(Order).where(Order.id == order_id)
        return await self.session.scalar(statement=statement)

    async def get_by_order_id(self, order_id: int) -> Order | None:
        statement = select(Order).where(Order.order_id == order_id)
        return await self.session.scalar(statement=statement)

    async def get_by_sub_merchant_id(self, sub_merchant_id: int) -> Order | None:
        statement = select(Order).where(Order.sub_merchant_id == sub_merchant_id)
        return await self.session.scalar(statement=statement)

    async def get_all(self) -> list[Order]:
        statement = select(Order).order_by(Order.id)
        result = await self.session.execute(statement=statement)
        return result.scalars().all()

    async def delete_all(self) -> None:
        await self.session.execute(delete(Order))
        await self.session.commit()

    async def delete_by_id(self, order_id: int) -> Order | None:
        _order = await self.get_by_id(order_id=order_id)
        statement = delete(Order).where(Order.id == order_id)
        await self.session.execute(statement=statement)
        await self.session.commit()
        return _order
