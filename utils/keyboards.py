from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Нажми меня", callback_data="button_pressed")],
            [InlineKeyboardButton(text="GitHub", callback_data="github_button")],
        ]
    )
    return keyboard

def main_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Мои финансы", callback_data="my_finances")],
            [InlineKeyboardButton(text="пустышка", callback_data="dummy_1")],
            [InlineKeyboardButton(text="пустышка", callback_data="dummy_2")]
        ]
    )
    return keyboard