import re
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import BotCommand, CallbackQuery, Message
from aiogram.filters import CommandStart, CommandObject
from bot import kb

from database import requests

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class Forms(StatesGroup):
    category = State()
    department = State()
    service = State()
    user_id = State()
    sub_category = State()

    code = State()
    ops = State()
    opsid = State()
    time = State()


base_command = [
    BotCommand(command='start', description='Главное меню')
]

base_router = Router()


@base_router.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    result = await requests.select_user(user_id)
    if result:
        await message.answer(text="Главное меню", reply_markup=kb.main_menu())
    else:
        await requests.add_new_users(user_id)
        await message.answer(text="Добро пожаловать!", reply_markup=kb.welcome())


@base_router.callback_query(F.data.in_(['main_menu']))
async def main_menu(call: CallbackQuery):
    await call.message.edit_text("Главное меню: ", reply_markup=kb.main_menu())


@base_router.callback_query(F.data.in_(['category']))
async def category(call: CallbackQuery, state: FSMContext):
    await state.set_state(Forms.category)
    await call.message.edit_text("Выберите желаемую категорию: ", reply_markup=kb.category())


@base_router.callback_query(F.data.in_(['M', 'MP', 'P', 'T', 'F', 'N', 'Z', 'A']))
async def sub_category(call: CallbackQuery, state: FSMContext):
    await state.update_data(category=call.data)

    if call.data in ['A', 'Z', 'N', 'F']:
        print('1')
        #await check(call)
    else:
        article = await requests.select_sub_category(call.data)
        await call.message.edit_text("Выберите желаемую ПОД-категорию: ", reply_markup=kb.sub_category(article))

@base_router.callback_query(F.data.in_(['show_ops']) | F.data.regexp(r'^category\d+$'))
async def main_menu(call: CallbackQuery, state: FSMContext):
    await state.update_data(sub_category=call.data)


    result = await requests.select_ops()
    await call.message.edit_text("Выберите ближайший к вам ОПС: ", reply_markup=kb.show_ops(result))


@base_router.callback_query(F.data.regexp(r'^ops\d+$'))
async def check(call: CallbackQuery, state: FSMContext):
    await state.update_data(ops=call.data)
    data = await state.get_data()

    category = data["category"]
    sub_category = data["sub_category"]
    ops = re.findall(r'\d+', data["ops"])

    msg = f"""======{ops[1]}=======
    
    """
    await call.message.edit_text(text=msg, reply_markup=kb.check())
