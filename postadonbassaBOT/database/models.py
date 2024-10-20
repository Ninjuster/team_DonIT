from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import asyncio

from sqlalchemy import Text, text, ForeignKey, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from settings import DB_URL

async_engine = create_async_engine(url=f'{DB_URL}', echo=True)
async_session = async_sessionmaker(async_engine)
class Base(DeclarativeBase):
    pass


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[str, mapped_column(Text, server_default=text("(datetime('now'))"), nullable=True)]


class TBUsers(Base):
    __tablename__ = "users1"
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(unique=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_operator: Mapped[bool] = mapped_column(default=False)


class TBSubCategory(Base):
    __tablename__ = "sub_category"
    id: Mapped[intpk]
    name: Mapped[str]
    article: Mapped[str]

class TBOps(Base):
    __tablename__ = "departments"
    id: Mapped[intpk]
    name: Mapped[str]
    address: Mapped[str]

class TBtickets(Base):
    __tablename__ = "tickets"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    department: Mapped[int] = mapped_column(nullable=True)
    service: Mapped[int] = mapped_column(nullable=True)
    time: Mapped[created_at]
    is_handling: Mapped[bool] = mapped_column(nullable=True)
    is_handled: Mapped[bool] = mapped_column(nullable=True)
    user: Mapped[int] = mapped_column(nullable=True)
    code: Mapped[str] = mapped_column(nullable=True)


async def create_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

#asyncio.run(create_table())