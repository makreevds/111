from aiogram import Router
from aiogram.types import CallbackQuery
from utils.keyboards import *
from aiogram.exceptions import TelegramBadRequest
from utils.text_utils import *
from database.database import get_user

router = Router()  # Создаем Router

# Обработчик кнопок основной клавиатуры
@router.callback_query(lambda c: c.data in ["my_finances", "help", "my_info"])
async def main_keyboard_handler(callback: CallbackQuery):
    try:
        if callback.data == "my_finances":
            text = text_my_finance
        elif callback.data == "help":
            text = text_help
        elif callback.data == "my_info":
            # Получаем user_id из callback
            user_id = callback.from_user.id
            user_data = get_user(user_id)
            text = text_my_info(user_data)
        await callback.message.edit_text(text, parse_mode="MarkdownV2", reply_markup=back_to_main_keyboard())
    except TelegramBadRequest:
        print('Ошибка клавиатуры - 1')
    await callback.answer()

# Обработчик нажатия на кнопку "В главное меню"
@router.callback_query(lambda c: c.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(text_main_menu, reply_markup=main_keyboard(), parse_mode="MarkdownV2")
    await callback.answer()
