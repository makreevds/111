from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command
from database.database import get_user
from utils.keyboards import *
from utils.text_utils import *

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(text_main_menu, reply_markup=main_keyboard(), parse_mode="MarkdownV2")