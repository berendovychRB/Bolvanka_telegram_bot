import logging

from aiogram import executor

from bot import set_default_commands, dp
from handlers import client

logging.basicConfig(level=logging.INFO)

client.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=set_default_commands)
