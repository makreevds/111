import re

def escape_markdown_v2(text: str) -> str:
    """Экранирует спецсимволы для MarkdownV2"""
    escape_chars = r"_[]()~`>#+-=|{}.!"
    return re.sub(f"([{re.escape(escape_chars)}])", r"\\\1", text)

text_main_menu = escape_markdown_v2(
        "💰 *Привет! Я твой финансовый помощник* 🚀\n\n"
        "Я помогу тебе отслеживать твои финансы, собирая данные с разных платформ.\n\n"
        "🔹 *Просматривай свои доходы и расходы*\n"
        "🔹 *Анализируй финансовую статистику*\n"
        "🔹 *Получай отчёты и уведомления*\n\n"
        "Начни с выбора раздела ниже ⬇️"
    )

text_my_finance = escape_markdown_v2(
    "*Раздел: Мои финансы*")

text_help = escape_markdown_v2(
    "Если у вас возникли проблемы или вопросы, не стесняйтесь обращаться:\n\n"
    "*Наш контакт для поддержки:* [@ustinov_ds](tg://user?id=ustinov_ds)\n\n"
    "Мы всегда рады помочь вам!")

def text_my_info(user_data):
    if user_data:
        text = (
        f"📋 Информация о пользователе:\n"
        f"🆔 ID: {user_data[0]}\n"
        f"👤 Username: @{user_data[1]}\n"
        f"👨‍💻 Имя: {user_data[2]}\n"
        f"👩‍💻 Фамилия: {user_data[3]}\n"
        f"🌐 Язык: {user_data[4]}\n"
        f"📅 Дата регистрации: {user_data[5]}\n"
        f"🕒 Последняя активность: {user_data[6]}\n"
        f"🔢 Количество взаимодействий: {user_data[7]}\n"
        f"📊 Статус: {user_data[8]}")
    else:
        text = "❌ Пользователь не найден в базе данных."
    text = escape_markdown_v2(text)
    return text