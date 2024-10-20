import asyncio
from sqlalchemy import select, insert, func
from database.models import async_session,create_table, TBUsers, TBSubCategory, TBOps



async def add_new_users(user_id):
    async with async_session() as session:
        stmt = insert(TBUsers).values(user_id=user_id)
        await session.execute(stmt)
        await session.commit()


async def select_user(user_id):
    async with async_session() as session:
        stmt = select(TBUsers).where(TBUsers.user_id == user_id)
        results = await session.execute(stmt)
        res = results.all()

        if res:
            return res

        return None

async def select_sub_category(article):
    async with async_session() as session:
        stmt = select(TBSubCategory).filter(TBSubCategory.article == article)
        results = await session.execute(stmt)
        res = results.scalars().all()

        if res:
            return res

        return None

async def select_ops():
    async with async_session() as session:
        stmt = select(TBOps)
        results = await session.execute(stmt)
        res = results.scalars().all()

        if res:
            return res

        return None



# async def main():
#     await create_table()
#     #await add_new_users(2)
#     #
#     # user = await select_user(1)
#     # print(user)
#
# asyncio.run(main())