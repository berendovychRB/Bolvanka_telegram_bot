from aiogram import Dispatcher, types

from config.languages import languages
from config.languages import default_language as d_lang
from services import user


async def start(message: types.Message):
    response = user.save_user(message=message)
    first_name = message.from_user.first_name

    if response["status_code"] == 200:
        await message.answer(
            f"{languages[d_lang]['hi']} {first_name}!\n{languages[d_lang]['welcome']}",
        )
    elif response["status_code"] == 409:
        await message.answer(
            f"{languages[d_lang]['comeback']} {first_name}!"
        )
    else:
        await message.answer(languages[d_lang]["error"])


async def echo(message: types.Message):
    await message.answer(message.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(echo)
