import asyncio
from aiogram import Dispatcher

from settings import bot
from logging_settings import log
from bot.base import base_command, base_router
from database import models
async def bot_start():
    try:
        dp = Dispatcher()
        dp.include_routers(base_router)

        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_my_commands(base_command)
        await dp.start_polling(bot)

    except:
        log.critical(f"Error: ", exc_info=True)

async def main():
    try:
        db_app = asyncio.create_task(models.create_table())
        bot_app = asyncio.create_task(bot_start())
        await asyncio.gather(bot_app, db_app)
    except:
        log.critical(f"Error: ", exc_info=True)

if __name__ == "__main__":
    asyncio.run(main())