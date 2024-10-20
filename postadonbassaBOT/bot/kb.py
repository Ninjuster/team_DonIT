from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def welcome():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Продолжить", callback_data='main_menu')
    )
    builder.adjust(1)
    return builder.as_markup()


def main_menu():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Взять новый талон", callback_data='category'),
        InlineKeyboardButton(text="Мои талоны", callback_data='my_ticket')
    )
    builder.adjust(1, 1)
    return builder.as_markup()

def show_ops(article):
    builder = InlineKeyboardBuilder()
    all_ops = article
    if all_ops:
        for ops in all_ops:
            builder.add(
                InlineKeyboardButton(text=ops.name, callback_data=f'ops{ops.id}')
            )
    builder.add(InlineKeyboardButton(text="⬅️ Вернуться", callback_data='main_menu'))
    builder.adjust(2)
    return builder.as_markup()

def category():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Почтовые отправления", callback_data='M'),
        InlineKeyboardButton(text="Почтовые переводы", callback_data='MP'),
        InlineKeyboardButton(text="Платежи", callback_data='P'),
        InlineKeyboardButton(text="Стартовые пакеты мобильных операторов", callback_data='T'),
        InlineKeyboardButton(text="Товары народного потребления", callback_data='F'),
        InlineKeyboardButton(text="Подписка на газеты и журналы", callback_data='N'),
        InlineKeyboardButton(text="Написать заявление/обращение", callback_data='Z'),
        InlineKeyboardButton(text="Выплата пенсий/пособий", callback_data='A'),
        InlineKeyboardButton(text="⬅️ Вернуться", callback_data='show_ops'),
    )
    builder.adjust(1)
    return builder.as_markup()


def sub_category(article: str):
    builder = InlineKeyboardBuilder()
    all_sub_category = article
    if all_sub_category:
        for category in all_sub_category:
            builder.add(
                InlineKeyboardButton(text=category.name, callback_data=f'category{category.id}')
            )
    builder.add(InlineKeyboardButton(text="⬅️ Вернуться", callback_data='category'))
    builder.adjust(1)
    return builder.as_markup()

def check():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Да, я хочу талон!", callback_data='allow_check'),
        InlineKeyboardButton(text="⬅️ Вернуться", callback_data='show_ops')
    )
    builder.adjust(1)
    return builder.as_markup()