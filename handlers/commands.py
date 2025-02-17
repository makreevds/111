from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command
from database.database import get_user
from utils.keyboards import *

router = Router()

# Список команд и их описаний
command_descriptions = {
    "start": "Запуск бота",
    "help": "Помощь",
    "buttons": "Показать inline-кнопки",
    "info": "Информация о пользователе",
}

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я твой бот 🚀\nИспользуй /help для списка команд.")

@router.message(Command("help"))
async def help_command(message: Message):
    commands_list = [f"/{cmd} - {desc}" for cmd, desc in command_descriptions.items()]
    response = "Список команд:\n" + "\n".join(commands_list)
    await message.answer(response)

@router.message(Command("buttons"))
async def send_buttons(message: Message):
    await message.answer("Выбери кнопку:", reply_markup=get_inline_keyboard())

@router.message(Command("info"))
async def cmd_info(message: types.Message):
    user_id = message.from_user.id
    user_data = get_user(user_id)

    if user_data:
        response = (
            f"📋 Информация о пользователе:\n"
            f"🆔 ID: {user_data[0]}\n"
            f"👤 Username: @{user_data[1]}\n"
            f"👨‍💻 Имя: {user_data[2]}\n"
            f"👩‍💻 Фамилия: {user_data[3]}\n"
            f"🌐 Язык: {user_data[4]}\n"
            f"📅 Дата регистрации: {user_data[5]}\n"
            f"🕒 Последняя активность: {user_data[6]}\n"
            f"🔢 Количество взаимодействий: {user_data[7]}\n"
            f"📊 Статус: {user_data[8]}"
        )
    else:
        response = "❌ Пользователь не найден в базе данных."

    await message.answer(response)