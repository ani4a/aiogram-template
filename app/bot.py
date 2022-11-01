from aiogram import Bot

from app.config_parse import parser


bot = Bot(parser()["telegram"]["api_key"], parse_mode="HTML")
