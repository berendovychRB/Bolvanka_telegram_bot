from aiogram import Bot, Dispatcher, types
from config.settings import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def set_default_commands(_):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Розпочати"),
        types.BotCommand("help", "Допомога")
    ])
