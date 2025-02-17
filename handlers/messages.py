from aiogram import Router
from aiogram.types import Message
from utils.text_utils import *
from utils.keyboards import *

router = Router()  # Создаем Router

@router.message()
async def echo_message(message: Message):
    text = escape_markdown_v2(f"*Извини, я не понимаю что ты хочешь!*")
    await message.answer(text, parse_mode="MarkdownV2", reply_markup=back_to_main_keyboard())
