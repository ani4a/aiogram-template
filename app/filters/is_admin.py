from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import BoundFilter
from aiogram import Bot

from typing import Union

from app.config_parse import parser


class IsAdmin(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: Union[Message, CallbackQuery]) -> bool:
        bot = Bot.get_current()
        chat_id = message.chat.id
        user_id = message.from_user.id
        result = await bot.get_chat_member(
            chat_id=chat_id,
            user_id=user_id,
        )
        return result.is_chat_admin()


def register(dp):
    dp.filters_factory.bind(IsAdmin,
                            event_handlers=[dp.message_handlers, dp.callback_query_handlers])
