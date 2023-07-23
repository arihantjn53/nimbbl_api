from typing import Annotated

from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


intpk = Annotated[int, mapped_column(primary_key=True, index=True, autoincrement=True)]
str64 = Annotated[str, 64]
str100 = Annotated[str, 100]
str128 = Annotated[str, 128]
str256 = Annotated[str, 256]
