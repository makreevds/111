from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_to_main_keybard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="В главное меню", callback_data="back_to_main")],
        ]
    )
    return keyboard

def main_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Мои финансы", callback_data="my_finances")],
            [InlineKeyboardButton(text="Помощь", callback_data="help")],
            [InlineKeyboardButton(text="пустышка", callback_data="dummy_2")]
        ]
    )
    return keyboard