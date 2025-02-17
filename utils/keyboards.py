from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Нажми меня", callback_data="button_pressed")],
            [InlineKeyboardButton(text="GitHub", callback_data="github_button")],
        ]
    )
    return keyboard
