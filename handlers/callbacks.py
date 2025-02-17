from aiogram import Router
from aiogram.types import CallbackQuery
from utils.keyboards import get_inline_keyboard, main_keyboard
from aiogram.exceptions import TelegramBadRequest

router = Router()  # Создаем Router

# Обработчик кнопок основной клавиатуры
@router.callback_query(lambda c: c.data in ["my_finances", "dummy_1", "dummy_2"])
async def main_keyboard_handler(callback: CallbackQuery):
    try:
        if callback.data == "my_finances":
            await callback.message.edit_text("Раздел: Мои финансы", reply_markup=main_keyboard())
        elif callback.data == "dummy_1":
            await callback.message.edit_text("Пустая кнопка 1", reply_markup=main_keyboard())
        elif callback.data == "dummy_2":
            await callback.message.edit_text("Пустая кнопка 2", reply_markup=main_keyboard())
    except TelegramBadRequest:
        pass
    await callback.answer()

# Обработчик кнопок дополнительной клавиатуры
@router.callback_query(lambda c: c.data in ["button_pressed", "github_button"])
async def inline_keyboard_handler(callback: CallbackQuery):
    try:
        if callback.data == "button_pressed":
            await callback.message.answer("Ты нажал кнопку: Нажми меня", reply_markup=get_inline_keyboard())
        elif callback.data == "github_button":
            await callback.message.edit_text("Ты нажал кнопку: GitHub", reply_markup=get_inline_keyboard())
    except TelegramBadRequest:
        pass
    await callback.answer()
