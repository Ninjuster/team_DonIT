import os
from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()

TG_OWNER_ID = 839405003

DB_URL = os.getenv('DB_URL')
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN,default=DefaultBotProperties(parse_mode='HTML'))
