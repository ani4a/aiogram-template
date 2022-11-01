from aiogram import types

from app.db import handlersList
from app.locales.en import HandlerStart


async def cmd_start(message: types.Message):
    await message.answer(HandlerStart.default)


def register(dp):
    handlername = "start"

    handlersList.append([handlername, HandlerStart.description])
    dp.register_message_handler(cmd_start, commands=handlername, is_admin=True)
