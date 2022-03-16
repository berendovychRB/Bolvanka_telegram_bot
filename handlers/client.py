from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from bot import bot
from config.languages import languages
from config.languages import default_language as d_lan
from services import user, film
from utils import keyboard as nav

data = {"name": None, "genre": None, "comments": None}
bot.state = None

NAME = 1
GENRE = 2
COMMENTS = 3


async def start(message: types.Message):
    response = user.save_user(message=message)
    first_name = message.from_user.first_name

    if response["status_code"] == 200:
        await message.answer(
            f"{languages[d_lan]['hi']} {first_name}!\n{languages[d_lan]['welcome']}",
            reply_markup=nav.menu
        )
    elif response["status_code"] == 409:
        await message.answer(
            f"{languages[d_lan]['comeback']} {first_name}!",
            reply_markup=nav.menu
        )
    else:
        await message.answer(languages[d_lan]["error"])


async def get_all_films(message: types.Message):
    await film.retrieve_films(message)


async def get_all_reviewed_films(message: types.Message):
    await film.retrieve_reviewed_films(message)


async def get_all_unreviewed_films(message: types.Message):
    await film.retrieve_unreviewed_films(message)


async def add_film(message: types.Message):
    # await message.reply(
    #     f"{languages[d_lan]['fillForm']}{languages[d_lan]['example']}{languages[d_lan]['note']}",
    #     reply_markup=nav.addMenu)
    # # await film.add_film(message)
    global data
    data = {"name": None, "genre": None, "comments": None}

    bot.send_message(message.chat.id, "add title, text, comments in separated messages\n\nnow write title")


async def add_tittle(message: types.Message):
    await message.answer(message.text)


async def add_genre(message: types.Message):
    pass


async def add_comment(message: types.Message):
    pass


async def cancel(message: types.Message):
    await message.answer(f"{languages[d_lan]['cancelAddingFilm']}",
                         reply_markup=nav.menu)
    bot.state = None


async def confirm(message: types.Message):
    await film.add_film(message)
    await message.answer(f"{languages[d_lan]['filmSaved']}",
                         reply_markup=nav.menu)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(add_film,
                                Text(contains=f"{languages[d_lan]['addFilm']}"))
    dp.register_message_handler(get_all_films,
                                Text(contains=f"{languages[d_lan]['allFilms']}"))
    dp.register_message_handler(get_all_reviewed_films,
                                Text(contains=f"{languages[d_lan]['reviewedFilms']}"))
    dp.register_message_handler(get_all_unreviewed_films,
                                Text(contains=f"{languages[d_lan]['unreviewedFilms']}"))
    dp.register_message_handler(add_tittle,
                                Text(contains=f"{languages[d_lan]['addTittle']}"))
    dp.register_message_handler(add_genre,
                                Text(contains=f"{languages[d_lan]['addGenre']}"))
    dp.register_message_handler(add_comment,
                                Text(contains=f"{languages[d_lan]['addComment']}"))
    dp.register_message_handler(cancel,
                                Text(contains=f"{languages[d_lan]['cancel']}"))
    dp.register_message_handler(confirm,
                                Text(contains=f"{languages[d_lan]['confirm']}"))
