from aiogram.types import TelegramObject
from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from database.database import upsert_user  # Используем относительный импорт

class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # Получаем информацию о пользователе из события
        user = data.get("event_from_user")
        if user:
            # Обновляем данные пользователя в базе данных
            upsert_user(
                user_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
                language_code=user.language_code
            )

        # Продолжаем обработку события
        return await handler(event, data)