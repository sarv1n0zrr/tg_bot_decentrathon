from datetime import datetime
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from aiogram.types import Message, TelegramObject


def office_hours() -> bool:
    return datetime.now().weekday() in (0, 1, 2, 3, 4) and datetime.now().hour in ([i for i in (range(8, 19))])


class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        if office_hours():
           return await handler(event, data)

        await event.answer('Working hours:\r\nMon-Fri from 8 a.m to 6 p.m. Come during business hours')