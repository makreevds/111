from aiogram import Router
from aiogram.types import CallbackQuery
from utils.keyboards import *
from aiogram.exceptions import TelegramBadRequest
from handlers.commands import command_descriptions
from utils.text_utils import *
router = Router()  # Создаем Router

# Обработчик кнопок основной клавиатуры
@router.callback_query(lambda c: c.data in ["my_finances", "help", "dummy_2"])
async def main_keyboard_handler(callback: CallbackQuery):
    try:
        if callback.data == "my_finances":
            text = escape_markdown_v2("*Раздел: Мои финансы*")
            await callback.message.edit_text(text, parse_mode="MarkdownV2", reply_markup=back_to_main_keybard())
        elif callback.data == "help":
            commands_list = [f"/{cmd} - {desc}" for cmd, desc in command_descriptions.items()]
            response = escape_markdown_v2("*Список команд*:\n" + "\n".join(commands_list))
            await callback.message.edit_text(response, parse_mode="MarkdownV2", reply_markup=back_to_main_keybard())
        elif callback.data == "dummy_2":
            await callback.message.edit_text("Пустая кнопка 2", reply_markup=main_keyboard())
    except TelegramBadRequest:
        pass
    await callback.answer()

# Обработчик нажатия на кнопку "В главное меню"
@router.callback_query(lambda c: c.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(text_main_menu, reply_markup=main_keyboard(), parse_mode="MarkdownV2")
    await callback.answer()
