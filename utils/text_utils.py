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