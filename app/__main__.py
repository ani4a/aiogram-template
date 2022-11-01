import asyncio
import logging

from aiogram import Dispatcher
from aiogram.types import BotCommand
from aiogram.types.bot_command_scope import BotCommandScopeDefault

from app.db import handlersList, db_init
from app.register_all import register_all
from app.bot import bot


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s|%(levelname)s|%(name)s|%(message)s",
        datefmt='%Y-%m-%d|%H:%M:%S',
    )

    dp = Dispatcher(bot)
    commands = []

    for i in handlersList:
        commands.append(BotCommand(
            command=i[0],
            description=i[1].capitalize()))
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

    register_all(dp)
    await db_init()

    try:
        await dp.start_polling()
    finally:
        session = await bot.get_session()
        if session:
            await session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
