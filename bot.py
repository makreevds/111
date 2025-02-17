import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import callbacks, commands, messages
from utils.middleware import UserMiddleware
from database.database import create_db

# Изменеие 1111111111111
# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

async def main():
    """Основная функция для запуска бота."""


    # Инициализация бота и диспетчера
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Создаём таблицу, если её нет
    create_db()

    # Подключаем middleware
    dp.update.middleware(UserMiddleware())

    # Подключаем все Router'ы
    dp.include_routers(
        commands.router,
        callbacks.router,
        messages.router,
    )

    # Запуск бота
    logger.info("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
