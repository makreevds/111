from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from utils.keyboards import get_inline_keyboard
from aiogram.exceptions import TelegramBadRequest

router = Router()  # Создаем Router

# Обработчик нажатия на inline-кнопку
@router.callback_query()
async def button_pressed(callback: CallbackQuery):
    try:
        # Проверяем, какая кнопка была нажата
        if callback.data == "button_pressed":
            # Отправляем ответ с той же клавиатурой
            await callback.message.answer(
                "Ты нажал кнопку: Нажми меня", 
                reply_markup=get_inline_keyboard()
            )
        elif callback.data == "github_button":
            # Редактируем сообщение
            await callback.message.edit_text(
                "Ты нажал кнопку: GitHub", 
                reply_markup=get_inline_keyboard()
            )
    except TelegramBadRequest:
        # Обработка ошибки, если сообщение уже было изменено или удалено
        pass
    # Закрываем callback (чтобы Telegram знал, что запрос обработан)
    await callback.answer()
