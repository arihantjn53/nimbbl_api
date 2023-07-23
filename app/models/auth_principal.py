import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, intpk, str128


class AuthPrincipal(Base):
    __tablename__ = "nimbbl_auth_principal"

    id: Mapped[intpk]
    access_key: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    access_secret: Mapped[str128]
    access_secret_hash: Mapped[str128]
    sub_merchant_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    active: Mapped[bool]
    type: Mapped[str128]
    token: Mapped[str] = mapped_column(String(256), index=True, unique=True)
    token_expiration: Mapped[datetime.datetime]
    last_accessed_on: Mapped[datetime.datetime]
    number_of_token_per_minute: Mapped[int]
